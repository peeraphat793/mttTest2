import tkinter as tk
import random
import base64

CELL = 30
ROWS = 15
COLS = 20

maze = [
"####################",
"#........##........#",
"#.####.#.##.#.####.#",
"#..................#",
"#.####.######.####.#",
"#..................#",
"#.####.#.##.#.####.#",
"#........##........#",
"#..................#",
"#.####.######.####.#",
"#..................#",
"#.####.#.##.#.####.#",
"#........##........#",
"#..................#",
"####################"
]

# 🎨 ICON (base64 ฝังในโค้ด ไม่ต้องใช้ Pillow)
ICON_DATA = """
AAABAAEAEBAAAAAAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAQAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
"""

class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=COLS*CELL, height=ROWS*CELL, bg="black")
        self.canvas.pack()

        self.player = [1, 1]
        self.ghost = [18, 13]
        self.score = 0

        root.bind("<KeyPress>", self.move)

        self.draw()
        self.update_ghost()

    def draw(self):
        self.canvas.delete("all")

        for y in range(ROWS):
            for x in range(COLS):
                c = maze[y][x]
                if c == "#":
                    self.canvas.create_rectangle(
                        x*CELL, y*CELL,
                        x*CELL+CELL, y*CELL+CELL,
                        fill="blue"
                    )
                else:
                    self.canvas.create_oval(
                        x*CELL+12, y*CELL+12,
                        x*CELL+18, y*CELL+18,
                        fill="white"
                    )

        px, py = self.player
        self.canvas.create_oval(
            px*CELL, py*CELL,
            px*CELL+CELL, py*CELL+CELL,
            fill="yellow"
        )

        gx, gy = self.ghost
        self.canvas.create_oval(
            gx*CELL, gy*CELL,
            gx*CELL+CELL, gy*CELL+CELL,
            fill="red"
        )

        self.canvas.create_text(
            100, 10,
            fill="white",
            text=f"Score: {self.score}"
        )

        if self.player == self.ghost:
            self.canvas.create_text(
                200, 200,
                fill="red",
                text="GAME OVER",
                font=("Arial", 30)
            )

    def move(self, event):
        dx, dy = 0, 0

        if event.keysym == "Left":
            dx = -1
        elif event.keysym == "Right":
            dx = 1
        elif event.keysym == "Up":
            dy = -1
        elif event.keysym == "Down":
            dy = 1

        nx = self.player[0] + dx
        ny = self.player[1] + dy

        if maze[ny][nx] != "#":
            self.player = [nx, ny]
            self.score += 1

        self.draw()

    def update_ghost(self):
        gx, gy = self.ghost
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        random.shuffle(dirs)

        for dx, dy in dirs:
            nx, ny = gx+dx, gy+dy
            if maze[ny][nx] != "#":
                self.ghost = [nx, ny]
                break

        self.draw()
        self.root.after(300, self.update_ghost)


root = tk.Tk()
root.title("Pac-Man Python 3.14")

# 🖥️ ใส่ไอคอน (ถ้า system รองรับ)
try:
    icon = base64.b64decode(ICON_DATA)
    with open("icon.ico", "wb") as f:
        f.write(icon)
    root.iconbitmap("icon.ico")
except:
    pass

game = Game(root)
root.mainloop()
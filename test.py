def calculate_bmi(weight_kg: float, height_cm: float) -> tuple[float, str]:
    """
    คำนวณ BMI จากน้ำหนัก(กก.) และส่วนสูง(ซม.)
    คืนค่าเป็น (bmi, หมวดหมู่)
    """
    if height_cm <= 0 or weight_kg <= 0:
        raise ValueError("น้ำหนักและส่วนสูงต้องมากกว่า 0")

    height_m = height_cm / 100.0
    bmi = weight_kg / (height_m ** 2)

    # จัดหมวดหมู่ตามเกณฑ์ WHO สำหรับผู้ใหญ่เอเชีย (อาจต่างไปตามประเทศ/แนวทาง)
    if bmi < 18.5:
        category = "น้ำหนักน้อย"
    elif bmi < 23:
        category = "น้ำหนักปกติ"
    elif bmi < 25:
        category = "น้ำหนักเกิน"
    elif bmi < 30:
        category = "อ้วนระดับ 1"
    else:
        category = "อ้วนระดับ 2"

    return round(bmi, 2), category


def main():
    try:
        weight = float(input("weight (kg): "))
        height = float(input("height (cm): "))
        bmi, cat = calculate_bmi(weight, height)
        print(f"BMI this {bmi} ({cat})")
    except ValueError as e:
        print(f"error: {e}")


if __name__ == "__main__":
    main()

"""
Write function bmi that calculates body mass index (bmi = weight / height2).
"""

def bmi(weight: float, height: float) -> str:
    """Рассчитывает индекс массы тела (BMI)"""
    calculate_bmi = weight / (height ** 2)

    if calculate_bmi <= 18.5:
        return "Underweight"

    elif calculate_bmi <= 25.0:
        return "Normal"

    elif calculate_bmi <= 30.0:
        return "Overweight"

    else:
        return "Obese"

if __name__ == "__main__":
    print(bmi(83, 1.85))
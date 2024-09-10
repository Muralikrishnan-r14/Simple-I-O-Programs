# BMI Calculator
def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    return weight / (height ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Healthy"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


# Input from user
try:
    weight = float(input("Enter your body weight in kilograms: "))
    height = float(input("Enter your height in centimeters: ")) / 100  # Convert to meters

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Output BMI and category
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are in the '{bmi_category(bmi)}' category.")

except ValueError as e:
    print(f"Input error: {e}")

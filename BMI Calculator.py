weight=int(input("Enter your body weight in kilograms:"))
height=float(input("Enter your height in meters:"))
bmi=weight/(height*height)
print("your bmi is",bmi)
if bmi<18.5:
    print("Feeling bad for you,You're in the underweight range")
elif 18.5<=bmi<=24.9:
    print("congrats,You're in the healthy range")
elif 25<=bmi<=29.9:
    print("Burn some,You're in the range of ovwerweight")
else:
    print("You're in the obese range,Its not good for health ")
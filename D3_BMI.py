###original source below###

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
### BMI = weight/ height^2
bmi = weight/height**2

if bmi <= 18.5:
    print("under weight")
elif 18.5 < bmi <= 25:
    print("normol weight")
elif 25 < bmi <= 30:
    print("overweight")
elif 30 < bmi <= 35:
    print("obse")
else:
    print("clinically obse")

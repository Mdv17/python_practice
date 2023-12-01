hieght = float(input("What is your hieght in meters (e.g 70.5): "))
weight = float(input("What is your weight in kgs (e.g 1.70): "))

bmi = float(weight / (hieght * 2))

print("hieght: ", hieght, "m")
print("weight: ", weight, "kg")

print("Your BMI is: ", round(bmi,2))


if(bmi <= 18.5):
    print("You are underweight")

elif(bmi > 18.5 and bmi <= 24.9):
    print("You have normal weight")

elif(bmi > 24.9 and bmi <= 29.9):
    print("You are overweight")

else:
    print("You are overweight")
                   

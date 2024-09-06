weight = input(" pls input weight: ")
height = input (" pls input height in m: ")


BMI = float(weight)/(float(height)*float(height))

print("your BMI is: ",round(BMI,2))

if BMI < 18.5:
    print("under weight")
elif BMI >18.5 and BMI <18.5:
    print("normal weight")
elif BMI >25 and BMI <130:
    print("slightly over weight")
elif BMI >30 and BMI <35:
    print("obese weight")
else:
    print("clinically weight")
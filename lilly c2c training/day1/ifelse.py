height = float(input("enter height in cm: "))

 
if height > 120:
    print("he can ride")
    age = float(input("enter age: "))
    if age < 12:
        print("pay 50")
    elif age >12 and age<18:
        print("pay 100")
    else:
        print ("pay 150")

else:
    print("he can't ride")
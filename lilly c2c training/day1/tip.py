bill = float(input("Input the bill: "))
people = int(input("enter the number of people: "))
tip_percentage = float(input("enter the tip percentage: "))

tip = bill * tip_percentage/100

total = bill + tip

split = round(total/ people,2)

print('split:', split)


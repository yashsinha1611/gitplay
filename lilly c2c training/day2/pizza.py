total_bill = 0

while True:
    # Get pizza size
    pizza_size = input("Size (small, med, large): ").lower()
    if pizza_size == 'small':
        bill = 15
    elif pizza_size == 'med':
        bill = 20
    elif pizza_size == 'large':
        bill = 25
    else:
        print("Invalid size entered. Please try again.")
        continue  # Go back to the start of the loop

    # Get pepperoni choice
    pepperoni = input("Do you want pepperoni (true/false): ").strip().lower()
    if pepperoni == 'true':
        if pizza_size == 'small':
            bill += 2
        else:
            bill += 3

    # Get extra cheese choice
    extra_cheese = input("Do you need extra cheese (true/false): ").strip().lower()
    if extra_cheese == 'true':
        bill += 1

    # Add current pizza's bill to the total bill
    total_bill += bill

    # Ask if the user wants to add another pizza
    another_pizza = input("Would you like to add another pizza? (yes/no): ").strip().lower()
    if another_pizza != 'yes':
        break  # Exit the loop if the user doesn't want to add another pizza

print("Total bill: $", total_bill)

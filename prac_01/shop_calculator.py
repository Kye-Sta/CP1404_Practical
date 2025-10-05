
total_price = 0
number_of_items = int(input("Enter the amount of items:"))

for i in range(number_of_items):
    price = float(input("Price of Items:"))
    while price <= 0:
        print("Invalid input. Please enter a positive price.")
        price = float(input(f"Price of item:"))
    total_price += price

if total_price >= 100:
    total_price = total_price * 0.9

print(f"Total price for {number_of_items} items is ${total_price:.2f}")



total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(1, number_of_items + 1):
    price = float(input("Price of item: "))
    total = total + price
if total > 100:
    total = total * 90 / 100
print(f"Total price for {number_of_items} items is ${total:.2f}")

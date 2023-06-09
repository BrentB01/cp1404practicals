total_price = 0
while True:
    n_items = int(input("Number of items: "))
    if n_items < 0:
        print("Invalid number of items!")
    else:
        break
for i in range(1, n_items+1):
    p_item = float(input("Price of item: "))
    total_price += p_item
print(f"Total price for the {n_items} items is ${total_price:.2f}")

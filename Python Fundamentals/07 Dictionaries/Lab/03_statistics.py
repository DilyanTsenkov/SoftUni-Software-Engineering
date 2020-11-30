bakery = {}

while True:
    product = input()
    if product == "statistics":
        break

    food, quantity = product.split(": ")
    quantity = int(quantity)

    if food in bakery:
        bakery[food] += quantity
    else:
        bakery[food] = quantity

print("Products in stock:")

for product, quantity in bakery.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(bakery)}")
print(f"Total Quantity: {sum(bakery.values())}")

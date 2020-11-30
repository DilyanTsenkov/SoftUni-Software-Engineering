database_quantity = {}
database_price = {}

while True:
    product = input()
    if product == "buy":
        break

    name, price, quantity = product.split()
    price = float(price)
    quantity = int(quantity)

    if name not in database_quantity:
        database_quantity[name] = quantity
    else:
        database_quantity[name] += quantity

    database_price[name] = price

for product_quantity, quantity in database_quantity.items():
    for product_price, prices in database_price.items():
        if product_price == product_quantity:
            database_quantity[product_quantity] = quantity * prices
            break

    print(f"{product_quantity} -> {database_quantity[product_quantity]:.2f}")

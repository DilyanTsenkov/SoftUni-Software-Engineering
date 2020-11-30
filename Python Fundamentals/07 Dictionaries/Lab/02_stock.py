products_quantities = input().split()
products_to_find = input().split()

stock = {}

for i in range(0, len(products_quantities), 2):
    product = products_quantities[i]
    quantity = products_quantities[i + 1]
    stock[product] = quantity

for product in products_to_find:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

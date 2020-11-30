product_input = input()
quantity_input = int(input())


def order(product, quantity):
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00
    return price * quantity


print(f"{order(product_input, quantity_input):.2f}")

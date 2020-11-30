customer = ""
receipt = 0
total_prices = 0

while True:
    price = input()

    if price == "special" or price == "regular":
        customer = price
        break

    if float(price) < 0:
        print("Invalid price!")
    else:
        total_prices += float(price)

taxes = total_prices * 0.2
receipt = total_prices + taxes

if customer == "special":
    receipt *= 0.9

if receipt == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_prices:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {receipt:.2f}$")

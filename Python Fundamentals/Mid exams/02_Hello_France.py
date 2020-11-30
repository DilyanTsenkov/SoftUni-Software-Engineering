items_and_prices = input().split("|")
budget = float(input())

new_items_and_prices_list = []
increase_price = 0
increase_price_list = []
profit = 0
sum_increase_price = 0

for i in items_and_prices:
    item_type, price = i.split("->")
    price = float(price)

    is_valid = (item_type == "Clothes" and price <= 50) or (item_type == "Shoes" and price <= 35) or (
            item_type == "Accessories" and price <= 20.5)

    if is_valid and budget >= price:
        budget -= price
        increase_price = price * 1.4
        sum_increase_price += increase_price
        increase_price_list.append(f"{increase_price:.2f}")
        profit += ((price * 1.4) - price)

items_and_prices_print = " ".join(increase_price_list)

print(items_and_prices_print)
print(f"Profit: {profit:.2f}")

if (budget + sum_increase_price) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
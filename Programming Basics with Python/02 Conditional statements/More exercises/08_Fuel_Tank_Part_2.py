fuel = input().lower()
fuel_quantity = float(input())
card = input().lower()
diesel_price = 2.33
gasoline_price = 2.22
gas_price = 0.93
result = 0
if card == 'yes':
    diesel_price -= 0.12
    gasoline_price -= 0.18
    gas_price -= 0.08
if 20 <= fuel_quantity <= 25:
    discount = 0.92
elif fuel_quantity > 25:
    discount = 0.9
else:
    discount = 1
if fuel == 'diesel':
    result = diesel_price * discount * fuel_quantity
elif fuel == 'gasoline':
    result = gasoline_price * discount * fuel_quantity
elif fuel == 'gas':
    result = gas_price * discount * fuel_quantity
print(f'{result:.2f} lv.')
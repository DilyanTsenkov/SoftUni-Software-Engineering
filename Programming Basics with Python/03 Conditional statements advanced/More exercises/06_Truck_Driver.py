season = input().lower()
km_per_month = float(input())
price_per_km = 0
if km_per_month <= 5000:
    if season == "summer":
        price_per_km = 0.9
    elif season == "winter":
        price_per_km = 1.05
    else:
        price_per_km = 0.75
elif 5000 < km_per_month <= 10000:
    if season == "summer":
        price_per_km = 1.1
    elif season == "winter":
        price_per_km = 1.25
    else:
        price_per_km = 0.95
else:
    price_per_km = 1.45
profit = 4 * km_per_month * price_per_km
taxes = profit * 0.1
result = profit - taxes
print(f"{result:.2f}")

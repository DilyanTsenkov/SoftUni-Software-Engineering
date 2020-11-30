budget = float(input())
season = input().lower()
car_class = ""
car_type = "Jeep"
car_price = 0
if budget <= 100:
    car_class = "Economy class"
    if season == "summer":
        car_price = budget * 0.35
        car_type = "Cabrio"
    else:
        car_price = budget * 0.65
elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "summer":
        car_price = budget * 0.45
        car_type = "Cabrio"
    else:
        car_price = budget * 0.80
else:
    car_class = "Luxury class"
    car_price = budget * 0.9
print(f"{car_class}\n{car_type} - {car_price:.2f}")

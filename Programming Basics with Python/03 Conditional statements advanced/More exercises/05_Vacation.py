budget = float(input())
season = input().lower()
place_to_sleep = "Camp"
location = "Alaska"
holiday_price = 0
if budget <= 1000:
    if season == 'winter':
        location = "Morocco"
        holiday_price = budget * 0.45
    else:
        holiday_price = budget * 0.65
elif 1000 < budget <= 3000:
    place_to_sleep = "Hut"
    if season == 'winter':
        location = "Morocco"
        holiday_price = budget * 0.60
    else:
        holiday_price = budget * 0.80
else:
    place_to_sleep = "Hotel"
    holiday_price = budget * 0.9
    if season == 'winter':
        location = "Morocco"
print(f"{location} - {place_to_sleep} - {holiday_price:.2f}")

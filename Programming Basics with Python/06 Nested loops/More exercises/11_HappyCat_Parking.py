days = int(input())
hours = int(input())
all_day_parking = 0
for day in range(1, days + 1):
    day_parking = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 == 1:
            parking_price = 2.5
        elif day % 2 == 1 and hour % 2 == 0:
            parking_price = 1.25
        else:
            parking_price = 1
        day_parking += parking_price
    all_day_parking += day_parking
    print(f"Day: {day} - {day_parking:.2f} leva")
print(f"Total: {all_day_parking:.2f} leva")

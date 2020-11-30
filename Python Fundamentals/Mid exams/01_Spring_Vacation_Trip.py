days_trip = int(input())
budget = float(input())
group = int(input())
fuel_price_km = float(input())
food_expenses_person_day = float(input())
hotel_person_night = float(input())

hotel = group * hotel_person_night * days_trip
if group > 10:
    hotel *= 0.75

food = group * food_expenses_person_day * days_trip
total = hotel + food

continue_the_trip = True

for day in range(1, days_trip + 1):
    travel_distance = float(input())
    fuel = travel_distance * fuel_price_km
    total += fuel
    if total > budget:
        continue_the_trip = False
        break
    if day % 3 == 0 or day % 5 == 0:
        total *= 1.4
        if total > budget:
            continue_the_trip = False
            break
    if day % 7 == 0:
        total -= total / group

difference = abs(budget-total)

if continue_the_trip:
    print(f"You have reached the destination. You have {difference:.2f}$ budget left.")
else:
    print(f"Not enough money to continue the trip. You need {difference:.2f}$ more.")

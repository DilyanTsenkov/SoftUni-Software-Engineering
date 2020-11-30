season = input().lower()
group_type = input().lower()
count_students = int(input())
nights = int(input())
price_per_night = 0
sport = ""
if season == "winter":
    price_per_night = 9.6
    if group_type == "mixed":
        price_per_night = 10
        sport = "Ski"
    elif group_type == "girls":
        sport = "Gymnastics"
    else:
        sport = "Judo"
elif season == "spring":
    price_per_night = 7.2
    if group_type == "mixed":
        price_per_night = 9.5
        sport = "Cycling"
    elif group_type == "girls":
        sport = "Athletics"
    else:
        sport = "Tennis"
elif season == "summer":
    price_per_night = 15
    if group_type == "mixed":
        price_per_night = 20
        sport = "Swimming"
    elif group_type == "girls":
        sport = "Volleyball"
    else:
        sport = "Football"
costs = count_students * price_per_night *nights
if count_students >= 50:
    costs *= 0.5
elif 20 <= count_students < 50:
    costs *= 0.85
elif 10 <= count_students < 20:
    costs *= 0.95
print(f"{sport} {costs:.2f} lv.")

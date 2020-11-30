# ----------------------------------------------------08. Scholarship
import math
income = float(input())
average_success = float(input())
minimal_salary = float(input())
social_scholarship = 0
excellent_scholarship = 0
if average_success < 4.5 or (income > minimal_salary and average_success < 5.5):
    print("You cannot get a scholarship!")
if income < minimal_salary and average_success > 4.5:
    social_scholarship = math.floor(minimal_salary * 0.35)
if average_success >= 5.5:
    excellent_scholarship = math.floor(average_success * 25)
if social_scholarship != 0 or excellent_scholarship != 0:
    if social_scholarship <= excellent_scholarship:
        print(f"You get a scholarship for excellent results {excellent_scholarship:.0f} BGN")
    else:
        print(f"You get a Social scholarship {social_scholarship:.0f} BGN")
# ----------------------------------------------------07. World Swimming Record
import math
record_in_seconds = float(input())
distance_in_meters = float(input())
meter_per_second = float(input())
needed_time = distance_in_meters * meter_per_second
water_slow = math.floor(distance_in_meters / 15) * 12.5
result = needed_time + water_slow
if result >= record_in_seconds:
    print(f"No, he failed! He was {(result - record_in_seconds):.2f} seconds slower.")
else:
    print(f'Yes, he succeeded! The new world record is {result:.2f} seconds.')
# ----------------------------------------------------06. Godzilla vs. Kong
movie_budget = float(input())
people = int(input())
clothe_price_per_person = float(input())
decor_price = movie_budget * 0.1
clothe_price_for_all = people * clothe_price_per_person
if people > 150:
    clothe_price_for_all *= 0.9
needed_money = decor_price + clothe_price_for_all
result = abs(movie_budget - needed_money)
if needed_money <= movie_budget:
    print("Action!")
    print(f"Wingard starts filming with {result:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {result:.2f} leva more.")
# ----------------------------------------------------05. Time + 15 Minutes
hour = int(input())
minutes = int(input())
in_minutes = hour * 60 + minutes
after_fifteen_minutes = in_minutes + 15
hour = after_fifteen_minutes // 60
if hour > 23:
    hour = 0
minutes = after_fifteen_minutes % 60
print('%d:''%02d' % (hour, minutes))
# ----------------------------------------------------04. Metric Converter
length = float(input())
input_dimension = input()
output_dimension = input()
if input_dimension == 'mm':
    if output_dimension == 'm':
        length /= 1000
    elif output_dimension == 'cm':
        length /= 10
elif input_dimension == 'cm':
    if output_dimension == 'm':
        length /= 100
    elif output_dimension == 'mm':
        length *= 10
elif input_dimension == 'm':
    if output_dimension == 'mm':
        length *= 1000
    elif output_dimension == 'cm':
        length *= 100
print(f'{length:.3f}')
# ----------------------------------------------------03. Speed Info
speed = float(input())
result = ''
if speed <= 10:
    result = 'slow'
elif 10 < speed <= 50:
    result = 'average'
elif 50 < speed <= 150:
    result = 'fast'
elif 150 < speed <= 1000:
    result = 'ultra fast'
elif speed > 1000:
    result = 'extremely fast'
print(result)
# ----------------------------------------------------02. Bonus Score
points = int(input())
bonus_point = 0
if points <= 100:
    bonus_point = 5
elif 100 < points <= 1000:
    bonus_point = points * 0.2
elif points > 1000:
    bonus_point = points * 0.1
if points % 2 == 0:
    bonus_point += 1
elif points % 10 == 0:
    bonus_point += 2
print(bonus_point)
print(points + bonus_point)
# ----------------------------------------------------01. Sum Seconds
player_one = int(input())
player_two = int(input())
player_three = int(input())
all_seconds = player_one + player_two + player_three
in_minutes = all_seconds // 60
seconds = all_seconds % 60
print('%d:''%02d' % (in_minutes, seconds))

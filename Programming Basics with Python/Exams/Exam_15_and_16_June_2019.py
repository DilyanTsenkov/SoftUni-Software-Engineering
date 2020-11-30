# -----------------------------------------------------------------------06. Favorite Movie
movie = input()
counter = 0
max_points = 0
max_point_movie = ""
while movie != "STOP":
    counter += 1
    if counter == 7:
        print("The limit is reached.")
        break
    points = 0
    movie_length = len(movie)
    for letter in movie:
        char = ord(letter)
        if 64 < char < 91:
            char_points = char - movie_length
        elif 96 < char < 123:
            char_points = char - 2 * movie_length
        else:
            char_points = char
        points += char_points
    if points > max_points:
        max_point_movie = movie
        max_points = points
    movie = input()
print(f"The best movie for you is {max_point_movie} with {max_points} ASCII sum.")
# -----------------------------------------------------------------------06. Movie Tickets
a1 = int(input())
a2 = int(input())
n = int(input())
for first_symbol in range(a1, a2):
    for second_symbol in range(1, n):
        for third_symbol in range(1, n // 2):
            fourth_symbol = first_symbol
            if first_symbol % 2 == 1 and (second_symbol + third_symbol + first_symbol) % 2 == 1:
                print(f"{chr(first_symbol)}-{second_symbol}{third_symbol}{fourth_symbol}")
# -----------------------------------------------------------------------05. Series
budget = float(input())
tv_novels = int(input())
needed_money = 0
for tv_novel in range(tv_novels):
    tv_novel_name = input()
    tv_novel_price = float(input())
    if tv_novel_name == "Thrones":
        tv_novel_price *= 0.50
    elif tv_novel_name == "Lucifer":
        tv_novel_price *= 0.60
    elif tv_novel_name == "Protector":
        tv_novel_price *= 0.70
    elif tv_novel_name == "TotalDrama":
        tv_novel_price *= 0.80
    elif tv_novel_name == "Area":
        tv_novel_price *= 0.90
    needed_money += tv_novel_price
difference = abs(budget - needed_money)
if budget >= needed_money:
    print(f"You bought all the series and left with {difference:.2f} lv.")
else:
    print(f"You need {difference:.2f} lv. more to buy the series!")
# -----------------------------------------------------------------------05. Oscars
actor_name = input()
points = float(input())
judges = int(input())
for judge in range(judges):
    judge_name = input()
    judge_points = float(input())
    judge_name_length = len(judge_name)
    actor_points = judge_name_length * judge_points / 2
    points += actor_points
    if points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        break
if points <= 1250.5:
    print(f"Sorry, {actor_name} you need {(1250.5 - points):.1f} more!")
# -----------------------------------------------------------------------04. Cinema
hall_capacity = int(input())
profit = 0
tickets_price = 0
while True:
    spectator = input()
    if spectator == "Movie time!":
        print(f"There are {hall_capacity} seats left in the cinema.")
        break
    if hall_capacity < int(spectator):
        print("The cinema is full.")
        break
    if int(spectator) % 3 == 0:
        tickets_price = int(spectator) * 5 - 5
    else:
        tickets_price = int(spectator) * 5
    profit += tickets_price
    hall_capacity -= int(spectator)
print(f"Cinema income - {profit} lv.")
# -----------------------------------------------------------------------04. Movie Stars
budget = float(input())
while True:
    actor_name = input()
    if actor_name == "ACTION":
        print(f"We are left with {budget:.2f} leva.")
        break
    actor_name_length = len(actor_name)
    if actor_name_length <= 15:
        actor_salary = float(input())
    else:
        actor_salary = 0.2 * budget
    budget -= actor_salary
    if budget <= 0:
        print(f"We need {abs(budget):.2f} leva for our actors.")
        break
# -----------------------------------------------------------------------03. Film Premiere
movie = input()
extras = input()
tickets = int(input())
price = 0
if movie == "John Wick":
    if extras == "Drink":
        price = 12
    elif extras == "Popcorn":
        price = 15
    else:
        price = 19
elif movie == "Star Wars":
    if extras == "Drink":
        price = 18
    elif extras == "Popcorn":
        price = 25
    else:
        price = 30
else:
    if extras == "Drink":
        price = 9
    elif extras == "Popcorn":
        price = 11
    else:
        price = 14
if movie == "Star Wars" and tickets >= 4:
    price *= 0.7
elif movie == "Jumanji" and tickets == 2:
    price *= 0.85
bill = tickets * price
print(f"Your bill is {bill:.2f} leva.")
# -----------------------------------------------------------------------03. Movie Destination
budget = float(input())
destination = input()
season = input()
days = int(input())
price = 0
if destination == "Dubai":
    if season == "Winter":
        price = 45000
    else:
        price = 40000
elif destination == "Sofia":
    if season == "Winter":
        price = 17000
    else:
        price = 12500
else:
    if season == "Winter":
        price = 24000
    else:
        price = 20250
costs = days * price
if destination == "Dubai":
    costs *= 0.7
elif destination == "Sofia":
    costs *= 1.25
difference = abs(budget - costs)
if budget >= costs:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")
# -----------------------------------------------------------------------02. Lunch Break
import math

tv_novel = input()
episode_duration = int(input())
relax_duration = int(input())
lunch_time = relax_duration / 8
nothing_to_do_time = relax_duration / 4
time_to_watch = relax_duration - lunch_time - nothing_to_do_time
difference = abs(time_to_watch - episode_duration)
if time_to_watch >= episode_duration:
    print(f"You have enough time to watch {tv_novel} and left with {math.ceil(difference)} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_novel}, you need {math.ceil(difference)} more minutes.")
# -----------------------------------------------------------------------02. Movie Day
shooting_time = int(input())
scenes = int(input())
scene_time = int(input())
shooting_time_needed = shooting_time * 0.15 + (scenes * scene_time)
difference = abs(shooting_time - shooting_time_needed)
if shooting_time > shooting_time_needed:
    print(f"You managed to finish the movie on time! You have {round(difference)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(difference)} minutes.")
#-----------------------------------------------------------------------01. Series Calculator
import math

tv_novel = input()
seasons = int(input())
episodes = int(input())
time_no_commercials = float(input())
commercials = time_no_commercials * 0.2
one_episode = time_no_commercials + commercials
last_episode = seasons * 10
needed_time = one_episode * episodes * seasons + last_episode
print(f"Total time needed to watch the {tv_novel} series is {math.floor(needed_time)} minutes.")
# -----------------------------------------------------------------------01. Movie Profit
movie = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
percent_for_theater = int(input())
income = ticket_price * tickets * days
for_theater = income * percent_for_theater / 100
profit = income - for_theater
print(f"The profit from the movie {movie} is {profit:.2f} lv.")

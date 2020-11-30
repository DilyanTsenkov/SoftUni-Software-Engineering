# --------------------------------------------------06. High Jump
target_height = int(input())
starting_height = target_height - 30
height = starting_height
jump_counter = 0
breaker = False
while True:
    failure = 0
    for jump in range(3):
        jump_height = int(input())
        jump_counter += 1
        if jump_height > target_height and height == target_height:
            print(f"Tihomir succeeded, he jumped over {height}cm after {jump_counter} jumps.")
            breaker = True
            break
        elif jump_height > height:
            height += 5
            break
        else:
            failure += 1
        if failure == 3:
            print(f"Tihomir failed at {height}cm after {jump_counter} jumps.")
            breaker = True
    if breaker:
        break
# --------------------------------------------------06. Basketball Tournament
counter_wins = 0
counter = 0
while True:
    tournament_name = input()
    if tournament_name == "End of tournaments":
        percent_wins = counter_wins / counter * 100
        print(f"{percent_wins:.2f}% matches win")
        print(f"{(100 - percent_wins):.2f}% matches lost")
        break
    games = int(input())
    for game in range(1, games + 1):
        desi_team = int(input())
        other_team = int(input())
        difference = abs(desi_team - other_team)
        counter += 1
        if desi_team > other_team:
            counter_wins += 1
            print(f"Game {game} of tournament {tournament_name}: win with {difference} points.")
        else:
            print(f"Game {game} of tournament {tournament_name}: lost with {difference} points.")
# --------------------------------------------------05. Tennis Ranklist
import math

tournaments = int(input())
start_points = int(input())
tournament_points = 0
wins = 0
for tournament in range(tournaments):
    result = input()
    if result == "W":
        tournament_points += 2000
        wins += 1
    elif result == "F":
        tournament_points += 1200
    else:
        tournament_points += 720
total_points = start_points + tournament_points
average = tournament_points / tournaments
wins_percent = wins / tournaments * 100
print(f"Final points: {math.trunc(total_points)}")
print(f"Average points: {math.trunc(average)}")
print(f"{wins_percent:.2f}%")
# --------------------------------------------------05. Fitness Center
sportsman = int(input())
back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0
for sportsmen in range(sportsman):
    product = input()
    if product == "Back":
        back += 1
    elif product == "Chest":
        chest += 1
    elif product == "Legs":
        legs += 1
    elif product == "Abs":
        abs += 1
    elif product == "Protein shake":
        protein_shake += 1
    elif product == "Protein bar":
        protein_bar += 1
protein_percent = (protein_bar + protein_shake) / sportsman * 100
print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{(100 - protein_percent):.2f}% - work out")
print(f"{protein_percent:.2f}% - protein")
# --------------------------------------------------04. Game Number Wars
player_one = input()
player_two = input()
player_one_points = 0
player_two_points = 0
while True:
    player_one_card = input()
    if player_one_card == "End of game":
        print(f"{player_one} has {player_one_points} points")
        print(f"{player_two} has {player_two_points} points")
        break
    player_two_card = int(input())
    result = abs(int(player_one_card) - player_two_card)
    if int(player_one_card) > player_two_card:
        player_one_points += result
    elif int(player_one_card) < player_two_card:
        player_two_points += result
    else:
        player_one_card = input()
        player_two_card = int(input())
        print("Number wars!")
        if int(player_one_card) > player_two_card:
            print(f"{player_one} is winner with {player_one_points} points")
        elif int(player_one_card) < player_two_card:
            print(f"{player_two} is winner with {player_two_points} points")
        break
# -----------------------------------------------------04. Darts
players_name = input()
game_points = 301
counter_positive = 0
counter_negative = 0
while game_points != 0:
    sector = input()
    if sector == "Retire":
        break
    points = int(input())
    if sector == "Double":
        points *= 2
    elif sector == "Triple":
        points *= 3
    if points <= game_points:
        game_points -= points
        counter_positive += 1
    else:
        counter_negative += 1
if sector == "Retire":
    print(f"{players_name} retired after {counter_negative} unsuccessful shots.")
else:
    print(f"{players_name} won the leg with {counter_positive} shots.")
# --------------------------------------------------03. Gymnastics
nation = input()
discipline = input()
if nation == "Russia":
    if discipline == "ribbon":
        result = 9.1 + 9.4
    elif discipline == "hoop":
        result = 9.3 + 9.8
    else:
        result = 9.6 + 9
elif nation == "Bulgaria":
    if discipline == "ribbon":
        result = 9.6 + 9.4
    elif discipline == "hoop":
        result = 9.55 + 9.75
    else:
        result = 9.5 + 9.4
else:
    if discipline == "ribbon":
        result = 9.2 + 9.5
    elif discipline == "hoop":
        result = 9.45 + 9.35
    else:
        result = 9.7 + 9.15
difference = 20 - result
percent = difference / 20 * 100
print(f"The team of {nation} get {result:.3f} on {discipline}.")
print(f"{percent:.2f}%")
# -----------------------------------------------------03. World Snooker Championship
final = input()
ticket_type = input()
tickets = int(input())
shot = input()
ticket_price = 0
if final == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = 55.50
    elif ticket_type == "Premium":
        ticket_price = 105.20
    else:
        ticket_price = 118.90
elif final == "Semi final":
    if ticket_type == "Standard":
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    else:
        ticket_price = 300.40
else:
    if ticket_type == "Standard":
        ticket_price = 110.10
    elif ticket_type == "Premium":
        ticket_price = 160.66
    else:
        ticket_price = 400
shots = 0
costs = tickets * ticket_price
if shot == "Y":
    shots = tickets * 40
if costs > 4000:
    costs *= 0.75
elif costs > 2500:
    costs = costs * 0.9 + shots
else:
    costs += shots
print(f"{costs:.2f}")
# --------------------------------------------------02. Football Results
won = 0
loss = 0
draws = 0
for result in range(0, 3):
    game = input()
    if game[:-2] > game[2:]:
        won += 1
    elif game[:-2] < game[2:]:
        loss += 1
    else:
        draws += 1
print(f"Team won {won} games.\nTeam lost {loss} games.\nDrawn games: {draws}")
# -----------------------------------------------------02. Skeleton
minutes = int(input())
seconds = int(input())
length = float(input())
seconds_per_100 = int(input())
target_in_second = minutes * 60 + seconds
slow_down = length / 120 * 2.5
time = length / 100 * seconds_per_100 - slow_down
if time <= target_in_second:
    print(f"Marin Bangiev won an Olympic quota!\nHis time is {time:.3f}.")
else:
    print(f"No, Marin failed! He was {(time - target_in_second):.3f} second slower.")
# --------------------------------------------------01. Basketball Equipment
year_tax = int(input())
sneakers = 0.6 * year_tax
equip = 0.8 * sneakers
ball = 0.25 * equip
accessory = 0.20 * ball
needed_money = year_tax + sneakers + equip + ball + accessory
print(f"{needed_money:.2f}")
# -----------------------------------------------------01. Tennis Equipment
import math

rocket_price = float(input())
rockets = int(input())
sneakers = int(input())
rockets_and_sneakers = rockets * rocket_price + (sneakers * rocket_price / 6)
other = 0.2 * rockets_and_sneakers
costs = (rockets_and_sneakers + other) / 8
print(f"Price to be paid by Djokovic {math.floor(costs)}")
print(f"Price to be paid by sponsors {math.ceil(costs * 7)}")

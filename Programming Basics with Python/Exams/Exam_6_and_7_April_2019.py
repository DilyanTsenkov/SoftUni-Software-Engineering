#-----------------------------------------------------------06. Cinema Tickets
movie = input()
student = 0
standard = 0
kid = 0
all_tickets_sold = 0
while movie != "Finish":
    free_places = int(input())
    tickets_sold = 0
    while free_places > 0:
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student += 1
            free_places -= 1
            tickets_sold += 1
        elif ticket_type == "standard":
            standard += 1
            free_places -= 1
            tickets_sold += 1
        else:
            kid += 1
            free_places -= 1
            tickets_sold += 1
    all_tickets_sold += tickets_sold
    if free_places == 0:
        percent_full = 100
    else:
        percent_full = tickets_sold / (tickets_sold + free_places) * 100
    print(f"{movie} - {percent_full:.2f}% full.")
    movie = input()
percent_standard = standard / all_tickets_sold * 100
percent_student = student / all_tickets_sold * 100
percent_kid = kid / all_tickets_sold * 100
print(f"Total tickets: {all_tickets_sold}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")
#-----------------------------------------------------------05. Movie Ratings
movies = int(input())
max_rate = 0
max_rate_movie = ""
min_rate = 11
min_rate_movie = ""
all_movies_rating = 0
for movie in range(movies):
    movie_name = input()
    movie_rate = float(input())
    if max_rate < movie_rate:
        max_rate = movie_rate
        max_rate_movie = movie_name
    if min_rate > movie_rate:
        min_rate = movie_rate
        min_rate_movie = movie_name
    all_movies_rating += movie_rate
average_rate = all_movies_rating / movies
print(f"{max_rate_movie} is with highest rating: {max_rate}")
print(f"{min_rate_movie} is with lowest rating: {min_rate}")
print(f"Average rating: {average_rate:.1f}")
#-----------------------------------------------------------04. Cinema Voucher
voucher = int(input())
tickets = 0
others = 0
price = 0
while True:
    product = input()
    if product == "End":
        break
    if len(product) <= 8:
        first_symbol = ord(product[0])
        price = ord(product[0])
        if voucher < price:
            break
        others += 1
    else:
        first_symbol = ord(product[0])
        second_symbol = ord(product[1])
        price = ord(product[0]) + ord(product[1])
        if voucher < price:
            break
        tickets += 1
    voucher -= price
print(f"{tickets}")
print(f"{others}")
#-----------------------------------------------------------03. Oscars week in cinema
movie = input()
hall = input()
tickets = int(input())
price = 0
if hall == "normal":
    if movie == "A Star Is Born":
        price = 7.50
    elif movie == "Bohemian Rhapsody":
        price = 7.35
    elif movie == "Green Book":
        price = 8.15
    else:
        price = 8.75
elif hall == "luxury":
    if movie == "A Star Is Born":
        price = 10.5
    elif movie == "Bohemian Rhapsody":
        price = 9.45
    elif movie == "Green Book":
        price = 10.25
    else:
        price = 11.55
else:
    if movie == "A Star Is Born":
        price = 13.50
    elif movie == "Bohemian Rhapsody":
        price = 12.75
    elif movie == "Green Book":
        price = 13.25
    else:
        price = 13.95
print(f"{movie} -> {(price * tickets):.2f} lv.")
#-----------------------------------------------------------02. Godzilla vs. Kong
budget = float(input())
people = int(input())
cloths = float(input())
if people > 150:
    cloths *= 0.9
costs = budget * 0.1 + cloths * people
difference = abs(budget - costs)
if budget < costs:
    print(f"Not enough money!\nWingard needs {difference:.2f} leva more.")
else:
    print(f"Action!\nWingard starts filming with {difference:.2f} leva left.")
#-----------------------------------------------------------01. Oscars ceremony
rent = int(input())
costs = rent + 0.7 * rent + 0.7 * rent * 0.85 + 0.7 * rent * 0.85 / 2
print(f"{costs:.2f}")

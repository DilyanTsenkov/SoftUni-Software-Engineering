# ------------------------------------------------06. Cake
cake_width = int(input())
cake_length = int(input())
area = cake_length * cake_width
while area > 0:
    cake_pieces = input()
    if cake_pieces == "STOP":
        break
    area -= int(cake_pieces)
if area < 0:
    print(f"No more cake left! You need {abs(area)} pieces more.")
else:
    print(f"{area} pieces are left.")
# ------------------------------------------------05. Coins
change = float(input())
coins = change * 100
coin_2lv = coins // 200
coins = coins - coin_2lv * 200
coin_lv = coins // 100
coins = coins - coin_lv * 100
coin_50 = coins // 50
coins = coins - coin_50 * 50
coin_20 = coins // 20
coins = coins - coin_20 * 20
coin_10 = coins // 10
coins = coins - coin_10 * 10
coin_05 = coins // 5
coins = coins - coin_05 * 5
coin_02 = coins // 2
coins = coins - coin_02 * 2
coin_01 = coins // 1
coins = coins - coin_01 * 1
coins_counter = coin_2lv + coin_lv + coin_50 + coin_20 + coin_10 + coin_05 + coin_02 + coin_01
print(int(coins_counter))
# ------------------------------------------------04. Walking
steps_target = 10000
all_steps_made = 0
while all_steps_made < steps_target:
    steps_made = input()
    if steps_made == "Going home":
        steps_to_home = int(input())
        all_steps_made += steps_to_home
        break
    all_steps_made += int(steps_made)
step_diff = abs(all_steps_made - steps_target)
if all_steps_made >= steps_target:
    print(f"Goal reached! Good job!\n{step_diff} steps over the goal!")
else:
    print(f"{step_diff} more steps to reach goal.")
# ------------------------------------------------03. Vacation
excursion_price = float(input())
money_in_bank = float(input())
spending_days = 0
days = 0
while spending_days < 5 and money_in_bank < excursion_price:
    reaction = input()
    money = float(input())
    if reaction == "save":
        spending_days = 0
        money_in_bank += money
    if reaction == "spend":
        spending_days += 1
        money_in_bank -= money
        if money_in_bank < 0:
            money_in_bank = 0
    days += 1
if money_in_bank >= excursion_price:
    print(f"You saved the money for {days} days.")
if spending_days == 5:
    print(f"You can't save the money.\n{days}")
# ------------------------------------------------02. Exam Preparation
poor_score_attempts = int(input())
score_counter = 0
poor_score_counter = 0
problem_name_previous = ""
score_sum = 0
while poor_score_counter < poor_score_attempts:
    problem_name_input = input()
    if problem_name_input == "Enough":
        break
    score = int(input())
    if score <= 4:
        poor_score_counter += 1
    score_counter += 1
    score_sum += score
    problem_name_previous = problem_name_input
average_score = score_sum / score_counter
if problem_name_input == "Enough":
    print(
        f"Average score: {average_score:.2f}\nNumber of problems: {score_counter}\nLast problem: {problem_name_previous}")
elif score_counter >= poor_score_attempts:
    print(f"You need a break, {poor_score_attempts} poor grades.")
# ------------------------------------------------01. Old Books
book_name = input()
input_book = input()
book_counter = 0
while input_book != "No More Books":
    if book_name == input_book:
        break
    book_counter += 1
    input_book = input()
if book_name == input_book:
    print(f"You checked {book_counter} books and found it.")
elif input_book == "No More Books":
    print(f"The book you search is not here!\nYou checked {book_counter} books.")

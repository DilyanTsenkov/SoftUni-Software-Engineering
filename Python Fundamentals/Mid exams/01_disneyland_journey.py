costs = float(input())
months = int(input())

money_saved = 0

for month in range(1, months + 1):
    if month % 2 == 1 and months != 1:
        money_saved *= 0.84
    if month % 4 == 0:
        money_saved *= 1.25

    money_saved += (0.25 * costs)

difference = abs(money_saved - costs)

if money_saved >= costs:
    print(f"Bravo! You can go to Disneyland and you will have {difference:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {difference:.2f}lv. more.")

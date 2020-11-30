money = float(input())
year_to_live = int(input())
costs = 0
years = 17
for year in range(1800, year_to_live + 1):
    if year % 2 == 0:
        costs += 12000
        years += 1
    else:
        years += 1
        costs += 12000 + 50 * years
result = abs(money - costs)
if money >= costs:
    print(f"Yes! He will live a carefree life and will have {result:.2f} dollars left.")
else:
    print(f"He will need {result:.2f} dollars to survive.")

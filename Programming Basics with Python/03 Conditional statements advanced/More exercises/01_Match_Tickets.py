budget = float(input())
category = input()
people = int(input())
transport = 0
tickets = 0
if category == "VIP":
    tickets = 499.99 * people
elif category == "Normal":
    tickets = 249.99 * people
if 1 <= people <= 4:
    transport = budget * 0.75
elif 5 <= people <= 9:
    transport = budget * 0.60
elif 10 <= people <= 24:
    transport = budget * 0.50
elif 25 <= people <= 49:
    transport = budget * 0.40
elif people >= 50:
    transport = budget * 0.25
money_for_tickets = budget - transport
result = abs(money_for_tickets - tickets)
if money_for_tickets >= tickets:
    print(f"Yes! You have {result:.2f} leva left.")
else:
    print(f"Not enough money! You need {result:.2f} leva.")

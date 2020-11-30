juniors = int(input())
seniors = int(input())
trace = input()
junior_tax = 0
senior_tax = 0
if trace == "trail":
    junior_tax = 5.5
    senior_tax = 7
elif trace == "cross-country":
    junior_tax = 8
    senior_tax = 9.5
    if juniors + seniors >= 50:
        junior_tax *= 0.75
        senior_tax *= 0.75
elif trace == "downhill":
    junior_tax = 12.25
    senior_tax = 13.75
elif trace == "road":
    junior_tax = 20
    senior_tax = 21.5
income = juniors * junior_tax + seniors * senior_tax
tax = income * 0.05
donation = income - tax
print(f"{donation:.2f}")

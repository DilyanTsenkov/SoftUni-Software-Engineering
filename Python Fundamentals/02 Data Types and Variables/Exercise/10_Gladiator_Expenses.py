lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
counter_shield_broken = 0

for lost_fight in range(1, lost_fights_count + 1):
    if lost_fight % 2 == 0:
        expenses += helmet_price
    if lost_fight % 3 == 0:
        expenses += sword_price
    if lost_fight % 2 == 0 and lost_fight % 3 == 0:
        expenses += shield_price
        counter_shield_broken += 1
    if counter_shield_broken == 2:
        expenses += armor_price
        counter_shield_broken = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")

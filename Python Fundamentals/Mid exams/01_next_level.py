experience_needed = float(input())
count_of_battles = int(input())

experience = 0
battle_counter = 0
successfully = False

for battle in range(1, count_of_battles + 1):
    every_battle_exp = float(input())

    if battle % 3 == 0:
        every_battle_exp *= 1.15
    if experience_needed <= experience:
        successfully = True
        break
    if battle % 5 == 0:
        every_battle_exp *= 0.9
    if battle % 15 == 0:
        every_battle_exp *= 1.05

    experience += every_battle_exp
    battle_counter += 1

    if experience_needed <= experience:
        successfully = True
        break

experience_needed -= experience

if successfully:
    print(f"Player successfully collected his needed experience for {battle_counter} battles.")
else:
    print(f"Player was not able to collect the needed experience, {experience_needed:.2f} more needed.")

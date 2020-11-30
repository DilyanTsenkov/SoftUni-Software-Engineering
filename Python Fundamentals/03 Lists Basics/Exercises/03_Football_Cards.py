cards_input = set(input().split())

players_A_team = 11
players_B_team = 11
terminated = False

for card in cards_input:

    if card[0] == "A":
        players_A_team -= 1
    else:
        players_B_team -= 1

    if players_B_team < 7 or players_A_team < 7:
        terminated = True
        break

print(f"Team A - {players_A_team}; Team B - {players_B_team}")

if terminated:
    print("Game was terminated")

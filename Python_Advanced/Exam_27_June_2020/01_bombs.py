from collections import deque


def all_more_then_3(bombs):
    if bombs[60][1] >= 3 and bombs[40][1] >= 3 and bombs[120][1] >= 3:
        return True


def printer(bombs, bomb_effects, bomb_casings):
    if all_more_then_3(bombs):
        print("Bene! You have successfully filled the bomb pouch!")
    else:
        print("You don't have enough materials to fill the bomb pouch.")
    print(f"Bomb Effects: {', '.join(str(el) for el in bomb_effects) if bomb_effects else 'empty'} ")
    print(f"Bomb Casings: {', '.join(str(el) for el in bomb_casings) if bomb_casings else 'empty'} ")
    for key in bombs:
        print(f"{bombs[key][0]}: {bombs[key][1]}")


bomb_effects = deque(input().split(", "))
bomb_casings = input().split(", ")
bombs = {60: ["Cherry Bombs", 0], 40: ["Datura Bombs", 0], 120: ["Smoke Decoy Bombs", 0]}
while bomb_effects and bomb_casings:
    current_bomb_effects = bomb_effects.popleft()
    current_bomb_casings = bomb_casings.pop()
    bomb_mix = int(current_bomb_effects) + int(current_bomb_casings)
    if bomb_mix not in bombs:
        bomb_effects.appendleft(current_bomb_effects)
        current_bomb_casings = int(current_bomb_casings) - 5
        if current_bomb_casings > -1:
            bomb_casings.append(current_bomb_casings)
    else:
        bombs[bomb_mix][1] += 1
    if all_more_then_3(bombs):
        break

printer(bombs, bomb_effects, bomb_casings)

def all_heroes(count):
    my_heroes = {}
    for n in range(count):
        hero, hp, mp = input().split()
        hp = int(hp)
        mp = int(mp)
        if hero not in my_heroes:
            my_heroes[hero] = [hp, mp]
    return my_heroes


def cast_spell(mp, my_hero, second, third):
    if mp >= second:
        mp -= second
        print(f"{my_hero} has successfully cast {third} and now has {mp} MP!")
    else:
        print(f"{my_hero} does not have enough MP to cast {third}!")
    return mp


def take_damage(my_heroes, my_hero, second, third):
    my_heroes[my_hero][0] -= second
    if my_heroes[my_hero][0] <= 0:
        my_heroes.pop(my_hero)
        print(f"{my_hero} has been killed by {third}!")
    else:
        print(f"{my_hero} was hit for {second} HP by {third} and now has {my_heroes[my_hero][0]} HP left!")
    return my_heroes


def recharge_or_heal(second, hp_or_mp, max_pts):
    hp_or_mp += second
    if hp_or_mp > max_pts:
        recovered_amount = second - (hp_or_mp - max_pts)
        hp_or_mp = max_pts
    else:
        recovered_amount = second
    return hp_or_mp, recovered_amount


heroes = all_heroes(int(input()))

while True:
    command = input()
    if command == "End":
        break
    command = command.split(" - ")
    action = command[0]
    hero_name = command[1]

    if action == "CastSpell":
        heroes[hero_name][1] = cast_spell(heroes[hero_name][1], hero_name, int(command[2]), command[3])
    elif action == "TakeDamage":
        heroes = take_damage(heroes, hero_name, int(command[2]), command[3])
    elif action == "Recharge":
        max_points = 200
        heroes[hero_name][1], recovered = recharge_or_heal(int(command[2]), heroes[hero_name][1], max_points)
        print(f"{hero_name} recharged for {recovered} MP!")
    elif action == "Heal":
        max_points = 100
        heroes[hero_name][0], recovered = recharge_or_heal(int(command[2]), heroes[hero_name][0], max_points)
        print(f"{hero_name} healed for {recovered} HP!")

heroes = dict(sorted(heroes.items(), key=lambda x: (-x[1][0], x[0])))

for key, value in heroes.items():
    print(key)
    print(f"HP: {heroes[key][0]}")
    print(f"MP: {heroes[key][1]}")

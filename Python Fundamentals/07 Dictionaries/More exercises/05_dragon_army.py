def input_null_checker(my_input):
    d_type, d_name, d_damage, d_health, d_armor = my_input.split()
    if d_damage == "null":
        d_damage = 45
    if d_health == "null":
        d_health = 250
    if d_armor == "null":
        d_armor = 10
    return d_type, d_name, int(d_damage), int(d_health), int(d_armor)


def add_dragon(dragons, count_id, drag_type, drag_name, drag_damage, drag_health, drag_armor):
    if drag_type not in dragons:
        count_id += 1
        dragons[drag_type] = {count_id: [drag_name, drag_damage, drag_health, drag_armor]}
    else:
        is_found = False
        for key in dragons.keys():
            if is_found:
                break
            if key == drag_type:
                for value in dragons[drag_type].values():
                    if value[0] == drag_name:
                        value[1] = drag_damage
                        value[2] = drag_health
                        value[3] = drag_armor
                        is_found = True
                        break
        if not is_found:
            count_id += 1
            dragons[drag_type][count_id] = [drag_name, drag_damage, drag_health, drag_armor]
    return dragons, count_id


def calculation_and_print(dragons):
    for t, d in dragons.items():
        damage = 0
        health = 0
        armor = 0
        d = dict(sorted(d.items(), key=lambda x: x[1][0]))
        for k, v in d.items():
            damage += v[1]
            health += v[2]
            armor += v[3]
        damage /= len(d)
        health /= len(d)
        armor /= len(d)
        print(f'{t}::({damage:.2f}/{health:.2f}/{armor:.2f})')
        for value in d.values():
            print(f'-{value[0]} -> damage: {int(value[1])}, health: {int(value[2])}, armor: {int(value[3])}')


dragons_count = int(input())
count_id = 0
dragons = {}

for dragon in range(dragons_count):
    drag_type, drag_name, drag_damage, drag_health, drag_armor = input_null_checker(input())
    dragons, count_id = add_dragon(dragons, count_id, drag_type, drag_name, drag_damage, drag_health, drag_armor)

calculation_and_print(dragons)

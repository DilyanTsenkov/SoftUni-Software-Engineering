import re


def d_health(d):
    health_regex = r"[^0-9\.\+\*\/\-]"
    d_health = 0
    health_symbols = re.findall(health_regex, d)
    for symbol in health_symbols:
        d_health += ord(symbol)
    return d_health


def d_damage(d):
    damage_regex = r"(?P<damage>[-]?\d+(\.\d+)?)"
    d_damage = 0
    damage_symbols = re.finditer(damage_regex, d)
    for sym in damage_symbols:
        dic = sym.groupdict()
        d_damage += float(dic["damage"])
    return d_damage


def multi_div_sym(d, damage):
    mplying_dividing_regex = r"([\*\/])"
    multi_div_symbols = re.findall(mplying_dividing_regex, d)
    for symbol in multi_div_symbols:
        if symbol == "*":
            damage *= 2
        else:
            damage /= 2
    return damage


all_demons = input().split(",")
all_demons = [demon.strip() for demon in all_demons]
all_demons.sort()
demon_list = []

for demon in all_demons:
    demon_health = d_health(demon)
    demon_damage = d_damage(demon)
    demon_damage = multi_div_sym(demon, demon_damage)

    demon_string = f"{demon} - {demon_health} health, {demon_damage:.2f} damage"
    demon_list.append(demon_string)

for demon in demon_list:
    print(demon, end="\n")

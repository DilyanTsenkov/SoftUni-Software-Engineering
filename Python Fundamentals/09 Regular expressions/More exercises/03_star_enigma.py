import re


def key_finder(msgs):
    dcr_messages = []
    for n in range(msgs):
        message = input()
        regex = r"[star]"
        star = re.findall(regex, message, re.IGNORECASE)
        key = len(star)
        decrypted = ""
        for char in message:
            decrypted += chr(ord(char) - key)
        dcr_messages.append(decrypted)
    return dcr_messages


def planet_sort(dcr_messages):
    a_planets = []
    d_planets = []
    for msg in dcr_messages:
        regex = r"@(?P<planet>[A-za-z]+)([^@\-\!\:\>]+)?:(?P<population>\d+)([^@\-\!\:\>]+)?\!(?P<type>[AD])\!([^@\-\!\:\>]+)?->(?P<soldiers>\d+)"
        msg = re.finditer(regex, msg)
        for data in msg:
            d = data.groupdict()
            planet = d["planet"]
            type = d["type"]
            if type == "A":
                a_planets.append(planet)
            else:
                d_planets.append((planet))
    a_planets.sort()
    d_planets.sort()
    return a_planets, d_planets


message_count = int(input())
decrypted_messages = key_finder(message_count)
attacked_planets, destroyed_planets = planet_sort(decrypted_messages)

print(f"Attacked planets: {len(attacked_planets)}")
for planet in attacked_planets:
    print(f"-> {planet}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in destroyed_planets:
    print(f"-> {planet}")

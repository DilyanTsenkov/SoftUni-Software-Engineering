dungeons_rooms = input().split("|")
dungeons_rooms = [el.split() for el in dungeons_rooms]

room_counter = 0
health = 100
coins = 0


def potion(health, num):
    health += num
    hp = num
    if health > 100:
        hp = num - (health - 100)
        health = 100
    print(f"You healed for {hp} hp.")
    print(f"Current health: {health} hp.")
    return health


def chest(coins, num):
    coins += num
    print(f"You found {number} bitcoins.")
    return coins


def monster(health, num, com, room_c):
    health -= num
    if health > 0:
        print(f"You slayed {com}.")
        return health
    else:
        print(f"You died! Killed by {com}.")
        print(f"Best room: {room_c}")
        return False


for room in dungeons_rooms:
    room_counter += 1
    command = room[0]
    number = int(room[1])

    if command == "potion":
        health = potion(health, number)

    elif command == "chest":
        coins = chest(coins, number)

    else:
        health = monster(health, number, command, room_counter)
        if not health:
            break

if health:
    print("You've made it!")
    print(f"Bitcoins: {coins}")
    print(f"Health: {health}")


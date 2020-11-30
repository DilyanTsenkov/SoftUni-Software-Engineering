def user_input(database, side, user):
    for sides, users in database.items():
        if user in users:
            return database
    if side not in database:
        database[side] = []
        database[side].append(user)
    else:
        if user not in database[side]:
            database[side].append(user)
    return database


def user_transfer(database, side, user):
    for sides, users in database.items():
        if user in database[sides]:
            database[sides].remove(user)
            return user_input(database, side, user)
    return user_input(database, side, user)


database = {}

while True:
    receive = input()
    if receive == "Lumpawaroo":
        break

    if " | " in receive:
        force_side, force_user = receive.split(" | ")
        database = user_input(database, force_side, force_user)
    elif " -> " in receive:
        force_user, force_side = receive.split(" -> ")
        database = user_transfer(database, force_side, force_user)
        print(f"{force_user} joins the {force_side} side!")

database = dict(sorted(database.items(), key=lambda k: (-len(k[1]), k[0])))

for f_side, f_user in database.items():
    if len(database[f_side]) > 0:
        print(f"Side: {f_side}, Members: {len(database[f_side])}")
        database[f_side] = sorted(database[f_side])
        for el in database[f_side]:
            print(f"! {el}")
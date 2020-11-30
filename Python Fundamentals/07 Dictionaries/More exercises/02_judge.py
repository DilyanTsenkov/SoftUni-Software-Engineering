def contest_validator(cont_db, c_user, user_db, cont, name, pt):
    cont_db[cont] = []
    cont_db[cont].append([name, pt])
    c_user[cont] = []
    c_user[cont].append(name)
    user_db[name] += pt
    return cont_db, c_user, user_db


def user_validator(cont_db, c_user, user_db, cont, name, pt):
    cont_db[cont].append([name, pt])
    c_user[cont].append(name)
    user_db[name] += pt
    return cont_db, c_user, user_db


def higher_score(cont_db, user_db, name, pt):
    for key, value in cont_db.items():
        for el in cont_db[key]:
            if el[0] == name:
                if el[1] <= pt:
                    user_db[name] -= el[1]
                    user_db[name] += pt
                    el[1] = pt
    return cont_db, user_db


contest_dbase = {}
user_dbase = {}
cont_user = {}

while True:
    receive = input()
    if receive == "no more time":
        break

    username, contest, points = receive.split(" -> ")
    points = int(points)

    if username not in user_dbase:
        user_dbase[username] = 0

    if contest not in contest_dbase:
        contest_dbase, cont_user, user_dbase = contest_validator(contest_dbase, cont_user, user_dbase, contest,
                                                                 username, points)
    elif contest in contest_dbase and username not in cont_user[contest]:
        contest_dbase, cont_user, user_dbase = user_validator(contest_dbase, cont_user, user_dbase, contest, username,
                                                              points)
    else:
        contest_dbase, user_dbase = higher_score(contest_dbase, user_dbase, username, points)

for key, value in contest_dbase.items():
    print(f"{key}: {len(cont_user[key])} participants")
    position = 1
    contest_dbase[key] = list(sorted(contest_dbase[key], key=lambda x: (-x[1], x[0])))
    for el in contest_dbase[key]:
        print(f"{position}. {el[0]} <::> {el[1]}")
        position += 1

print("Individual standings:")
user_dbase = dict(sorted(user_dbase.items(), key=lambda k: (-k[1], k[0])))
position = 1
for k, v in user_dbase.items():
    print(f"{position}. {k} -> {user_dbase[k]}")
    position += 1

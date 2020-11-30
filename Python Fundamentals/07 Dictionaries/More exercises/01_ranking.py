def contest_validator(dbase_f_receive, contest_s_receive, pass_s_receive):
    if contest_s_receive in dbase_f_receive:
        if pass_s_receive == dbase_f_receive[contest_s_receive]:
            return True


def user_operator(dbase_f_receive, contest_s_receive, user_s_receive, points_s_receive):
    if user_s_receive not in dbase_f_receive:
        dbase_f_receive[user_s_receive] = []
        dbase_f_receive[user_s_receive].append([contest_s_receive, points_s_receive])
    else:
        new_contest = True
        for key, value in dbase_f_receive.items():
            if key == user_s_receive:
                for el in dbase_f_receive[user_s_receive]:
                    if contest_s_receive in el:
                        new_contest=False
                        if el[1] < points_s_receive:
                            el[1] = points_s_receive
                            break
                        else:
                            break
        if new_contest:
            dbase_f_receive[user_s_receive].append([contest_s_receive, points])
    return dbase_f_receive


def best_result(dbase):
    max_points = 0

    for key, value in dbase.items():
        current_points = 0
        for el in value:
            current_points += el[1]
        if max_points < current_points:
            max_points = current_points
            the_best = key
    return max_points, the_best


contest_dbase = {}
while True:
    first_receive = input()
    if first_receive == "end of contests":
        break
    contest, password = first_receive.split(":")
    contest_dbase[contest] = password

user_dbase = {}
while True:
    second_receive = input()
    if second_receive == "end of submissions":
        break
    contest, password, username, points = second_receive.split("=>")
    points = int(points)
    is_valid = contest_validator(contest_dbase, contest, password)
    if is_valid:
        user_dbase = user_operator(user_dbase, contest, username, points)

user_dbase = dict(sorted(user_dbase.items(), key=lambda k: k[0]))

best = best_result(user_dbase)
print(f"Best candidate is {best[1]} with total {best[0]} points.")

print("Ranking:")
for key, value in user_dbase.items():
    print(key)
    user_dbase[key] = [sorted(user_dbase[key], key=lambda x: x[1], reverse=True)]
    for v in user_dbase[key]:
        for el in v:
            print(f"#  {el[0]} -> {el[1]}")

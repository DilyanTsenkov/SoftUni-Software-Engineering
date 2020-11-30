def stat(language, points):
    if name not in statistic:
        statistic[name] = points
    else:
        if statistic[name] < points:
            statistic[name] = points

    if language in language_submissions:
        language_submissions[language] += 1
    else:
        language_submissions[language] = 1
    return statistic, language_submissions


statistic = {}
language_submissions = {}

while True:
    receive = input()
    if receive == "exam finished":
        break

    receive = receive.split("-")
    name = receive[0]

    if "banned" in receive:
        del statistic[name]

    else:
        statistic, language_submissions = stat(receive[1], int(receive[2]))

statistic = dict(sorted(statistic.items(), key=lambda k: (-k[1], k[0])))
language_submissions = dict(sorted(language_submissions.items(), key=lambda k: (-k[1], k[0])))

print("Results:")
for name, points in statistic.items():
    print(f"{name} | {statistic[name]}")

print("Submissions:")
for language, submission in language_submissions.items():
    print(f"{language} - {language_submissions[language]}")

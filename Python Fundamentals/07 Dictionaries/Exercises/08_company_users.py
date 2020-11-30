database_company = {}

while True:
    receiving = input()
    if receiving == "End":
        break

    company, employ = receiving.split(" -> ")

    if company not in database_company:
        database_company[company] = []
        database_company[company].append(employ)
    else:
        if employ not in database_company[company]:
            database_company[company].append(employ)

database_company = dict(sorted(database_company.items(), key=lambda k: k[0]))

for company, employ in database_company.items():
    print(f"{company}")
    for el in database_company[company]:
        print(f"-- {el}")

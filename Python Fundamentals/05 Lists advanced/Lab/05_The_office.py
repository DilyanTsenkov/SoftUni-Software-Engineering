happiness = input().split()
happiness_factor = int(input())

happiness = [int(el) for el in happiness]

multiplying_happiness = list(map(lambda el: el * happiness_factor, happiness))
average = sum(multiplying_happiness) / len(multiplying_happiness)

above_average = [el for el in multiplying_happiness if el >= average]

if len(above_average) >= len(happiness) / 2:
    print(f"Score: {len(above_average)}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {len(above_average)}/{len(happiness)}. Employees are not happy!")

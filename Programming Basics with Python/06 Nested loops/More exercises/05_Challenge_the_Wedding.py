men = int(input())
women = int(input())
max_places = int(input())
counter = 0
no_more_tables = False
for man in range(1, men + 1):
    for woman in range(1, women + 1):
        counter += 1
        print(f"({man} <-> {woman})", end=" ")
        if counter == max_places:
            no_more_tables = True
            break
    if no_more_tables:
        break

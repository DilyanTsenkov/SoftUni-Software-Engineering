waiting_people = int(input())
lift = list(map(int, input().split()))

for i in range(len(lift)):
    free_places = 4 - lift[i]

    if free_places >= waiting_people:
        lift[i] += waiting_people
        waiting_people = 0
    else:
        waiting_people -= free_places
        lift[i] = 4

average_sum = sum(lift) / len(lift)
lift = [str(lift[i]) for i in range(len(lift))]

if waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
    print(" ".join(lift))
elif average_sum != 4:
    print("The lift has empty spots!")
    print(" ".join(lift))
else:
    print(" ".join(lift))

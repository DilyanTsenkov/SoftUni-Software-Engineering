rooms = int(input())

all_chairs = 0
all_people = 0

for room in range(1, rooms + 1):
    chairs, people = input().split()
    chairs = len(chairs)
    difference = abs(int(people) - int(chairs))

    if int(people) > int(chairs):
        print(f"{difference} more chairs needed in room {room}")

    all_chairs += int(chairs)
    all_people += int(people)

if all_chairs >= all_people:
    print(f"Game On, {all_chairs - all_people} free chairs left")

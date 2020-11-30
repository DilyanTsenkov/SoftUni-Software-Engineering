day_events = input().split("|")

new_day_events_list = []
energy = 100
coins = 100
close = False

for i in day_events:
    new_day_events_list.append(i.split("-"))

for i in range(len(new_day_events_list)):
    event = new_day_events_list[i][0]
    number = int(new_day_events_list[i][1])
    if event == "rest":
        if energy + number > 100:
            print(f"You gained {100 - energy} energy.")
            energy = 100
        else:
            print(f"You gained {number} energy.")
            energy += number
        print(f"Current energy: {energy}.")
    elif event == "order":
        if energy >= 30:
            print(f"You earned {number} coins.")
            coins += number
            energy -= 30
        else:
            energy += 50
            print("You had to rest!")
    elif event != "order" and event != "rest":
        if coins - number > 0:
            print(f"You bought {event}.")
            coins -= number
        else:
            print(f"Closed! Cannot afford {event}.")
            close = True
            break

if not close:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

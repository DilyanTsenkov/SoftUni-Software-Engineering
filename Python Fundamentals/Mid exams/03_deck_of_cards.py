cards = input().split(", ")
commands = int(input())

for command in range(commands):
    received_command = input().split(", ")
    action = received_command[0]
    element = received_command[1]

    if action == "Add":
        if element in cards:
            print("Card is already bought")
        else:
            print("Card successfully bought")
            cards.append(element)

    elif action == "Remove":
        if element in cards:
            print("Card successfully sold")
            cards.remove(element)
        else:
            print("Card not found")

    elif action == "Remove At":
        if int(element) not in range(len(cards)):
            print("Index out of range")
        else:
            cards.pop(int(element))
            print("Card successfully sold")

    elif action == "Insert":
        card_name = received_command[2]
        if int(element) not in range(len(cards)):
            print("Index out of range")
        else:
            if card_name not in cards:
                cards.insert(int(element), card_name)
                print("Card successfully bought")
            else:
                print("Card is already bought")

print(", ".join(cards))

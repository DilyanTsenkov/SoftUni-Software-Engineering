gifts_names = input().split(" ")
command = input()

while command != "No Money":
    command_list = command.split(" ")

    if command_list[0] == "OutOfStock":
        if command_list[1] in gifts_names:
            for i in range(len(gifts_names)):
                if gifts_names[i] == command_list[1]:
                    gifts_names[i] = "None"

    elif command_list[0] == "Required" and int(command_list[2]) > 0 and int(command_list[2]) <= int(
            len(gifts_names)) - 1:
        gifts_names[int(command_list[2])] = command_list[1]

    elif command_list[0] == "JustInCase":
        gifts_names[int(len(gifts_names)) - 1] = command_list[1]
    command = input()

for n in range(len(gifts_names)):
    if "None" in gifts_names:
        gifts_names.remove("None")

gifts_names_print = " ".join(gifts_names)

print(gifts_names_print)

def odd(input_password):
    raw_pass = ""
    for i in range(len(input_password)):
        if i % 2 != 0:
            raw_pass += input_password[i]
    print(raw_pass)
    return raw_pass


def cut(raw_pass, index, length):
    raw_pass = raw_pass[:index] + raw_pass[index + length:]
    print(raw_pass)
    return raw_pass


def substitute(raw_pass, substring, substitute):
    if substring in raw_pass:
        raw_pass = raw_pass.replace(substring, substitute)
        print(raw_pass)
    else:
        print("Nothing to replace!")
    return raw_pass


password = input()

while True:
    command = input()
    if command == "Done":
        break

    command = command.split(" ")
    action = command[0]

    if action == "TakeOdd":
        password = odd(password)
    elif action == "Cut":
        password = cut(password, int(command[1]), int(command[2]))
    elif action == "Substitute":
        password = substitute(password, command[1], command[2])

print(f"Your password is: {password}")

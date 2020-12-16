def case(username, low_up):
    if low_up == "lower":
        username = username.lower()
    elif low_up == "upper":
        username = username.upper()
    print(username)
    return username


def reverse(username, start_index, end_index):
    if (0 <= start_index <= end_index) and (start_index <= end_index < len(username)):
        sub_string = username[start_index:end_index + 1]
        print(sub_string[::-1])


def cut(username, substring):
    if substring in username:
        username = username.replace(substring, "")
        print(username)
    else:
        print(f"The word {username} doesn't contain {substring}.")
    return username


def replace(username, char):
    username = username.replace(char, "*")
    print(username)
    return username


def check(username, char):
    if char in username:
        print("Valid")
    else:
        print(f"Your username must contain {char}.")


username = input()

while True:
    commands = input()
    if commands == "Sign up":
        break
    commands = commands.split()
    action = commands[0]
    if action == "Case":
        username = case(username, commands[1])
    elif action == "Reverse":
        reverse(username, int(commands[1]), int(commands[2]))
    elif action == "Cut":
        username = cut(username, commands[1])
    elif action == "Replace":
        username = replace(username, commands[1])
    elif action == "Check":
        check(username, commands[1])

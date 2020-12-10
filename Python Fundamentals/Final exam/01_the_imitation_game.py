message = input()

while True:
    command = input()
    if command == "Decode":
        break
    command = command.split("|")
    action = command[0]
    if action == "Move":
        letters = int(command[1])
        message = message[letters:] + message[:letters]
    elif action == "Insert":
        index = int(command[1])
        value = command[2]
        message = message[:index] + value + message[index:]
    if action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")

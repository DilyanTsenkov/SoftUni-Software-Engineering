def add(users, username):
    if username not in users:
        users[username] = {"mails": []}
    else:
        print(f"{username} is already registered")
    return users


def send(users, username, emails):
    users[username]["mails"].append(emails)
    return users


def delete(users, username):
    if username not in users:
        print(f"{username} not found!")
    else:
        users.pop(username)
    return users


users = {}
while True:
    command = input()
    if command == "Statistics":
        break
    command = command.split("->")
    action = command[0]
    username = command[1]
    if action == "Add":
        users = add(users, username)
    elif action == "Send":
        users = send(users, username, command[2])
    elif action == "Delete":
        users = delete(users, username)

users = dict(sorted(users.items(), key=lambda x: (-len(x[1]["mails"]), x[0])))

print(f"Users count: {len(users)}")
for key, value in users.items():
    print(key)
    for mail in value["mails"]:
        print(f" - {mail}")

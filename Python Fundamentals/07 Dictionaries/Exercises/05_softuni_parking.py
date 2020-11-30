def register(username, plate):
    if username not in registered:
        registered[username] = plate
        print(f"{username} registered {plate} successfully")
    else:
        print(f"ERROR: already registered with plate number {plate}")
    return registered


def unregister(username):
    if username not in registered:
        print(f"ERROR: user {username} not found")
    else:
        print(f"{username} unregistered successfully")
        del registered[username]
    return registered


n = int(input())

registered = {}

for i in range(n):
    command = input().split()

    if command[0] == "register":
        registered = register(command[1], command[2])

    elif command[0] == "unregister":
        registered = unregister(command[1])

for username, plate in registered.items():
    print(f"{username} => {registered[username]}")

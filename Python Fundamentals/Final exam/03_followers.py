def new(my_dict, name):
    if name not in my_dict:
        my_dict[name] = {"likes": 0, "comments": 0}
    return my_dict


def like(my_dict, name, count):
    if name not in my_dict:
        my_dict[name] = {"likes": count, "comments": 0}
    else:
        my_dict[name]["likes"] += count
    return my_dict


def comment(my_dict, name):
    if name not in my_dict:
        my_dict[name] = {"likes": 0, "comments": 1}
    else:
        my_dict[name]["comments"] += 1
    return my_dict


def blocked(my_dict, name):
    if name not in my_dict:
        print(f"{name} doesn't exist.")
    else:
        my_dict.pop(name)
    return my_dict


followers = {}

while True:
    command = input()
    if command == "Log out":
        break
    command = command.split(": ")
    action = command[0]
    username = command[1]

    if action == "New follower":
        followers = new(followers, username)
    elif action == "Like":
        followers = like(followers, username, int(command[2]))
    elif action == "Comment":
        followers = comment(followers, username)
    elif action == "Blocked":
        followers = blocked(followers, username)

print(f"{len(followers)} followers")

followers = dict(sorted(followers.items(), key=lambda x: (-x[1]["likes"], x[0])))

for key, value in followers.items():
    print(f"{key}: {value['likes'] + value['comments']}")

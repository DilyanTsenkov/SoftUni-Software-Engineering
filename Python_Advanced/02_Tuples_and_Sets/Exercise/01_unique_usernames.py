n = int(input())

usernames = set()
for _ in range(n):
    username = input()
    usernames.add(username)

print("\n".join(usernames))

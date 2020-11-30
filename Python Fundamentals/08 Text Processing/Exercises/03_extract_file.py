path = input()
for n in range(len(path) - 1, 0, -1):
    if path[n] == "\\":
        index = n
        path = path[index + 1::]
        break

for el in path:
    if el == ".":
        index = path.index(el)

file_name = path[:index]
extension = path[index + 1::]

print(f"File name: {file_name}")
print(f"File extension: {extension}")

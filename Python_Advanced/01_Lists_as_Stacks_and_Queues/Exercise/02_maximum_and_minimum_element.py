queries = int(input())

stack = []

for _ in range(queries):
    query = input()
    if query.startswith("1"):
        query = query.split()
        stack.append(int(query[1]))
    elif len(stack) > 0:
        if query == "2":
            stack.pop()
        elif query == "3":
            print(max(stack))
        elif query == "4":
            print(min(stack))

if len(stack) > 0:
    while len(stack) > 1:
        print((stack.pop()), end=", ")
    print((stack.pop()))

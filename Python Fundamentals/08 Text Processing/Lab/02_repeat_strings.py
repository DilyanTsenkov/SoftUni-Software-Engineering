receive = input().split()

result = ""
for el in receive:
    result += el * len(el)

print(result)

text = input().split()

shortest = min(len(text[0]), len(text[1]))
total_sum = 0

for n in range(shortest):
    total_sum += ord(text[0][n]) * ord(text[1][n])

text[0] = text[0][shortest:]
text[1] = text[1][shortest:]
text = "".join(text)

for char in text:
    total_sum += ord(char)

print(total_sum)

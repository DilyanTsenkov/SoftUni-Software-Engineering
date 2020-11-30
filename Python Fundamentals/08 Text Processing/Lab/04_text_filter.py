ban_words = input().split(", ")
text = input()

for el in ban_words:
    if el in text:
        text = text.replace(el, "*" * len(el))

print(text)

import re

text = input()

regex = r"(?P<symbol>@|#)(?P<word_one>([A-za-z]+){3,})(?P=symbol){2}(?P<word_two>([A-za-z]+){3,})(?P=symbol)"

mirror_words = []

word_checker = re.findall(regex, text)
valid_pairs = len(word_checker)

word_checker = re.finditer(regex, text)
for item in word_checker:
    d = item.groupdict()
    if d["word_one"] == d["word_two"][::-1]:
        pair = d["word_one"] + " <=> " + d["word_two"]
        mirror_words.append(pair)

if valid_pairs:
    print(f"{valid_pairs} word pairs found!")
else:
    print("No word pairs found!")

if mirror_words:
    print("The mirror words are:")
    print(", ".join(mirror_words))
else:
    print("No mirror words!")

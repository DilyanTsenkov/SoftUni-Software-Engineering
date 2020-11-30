import re

sentence = input()
given_word = input()

match = re.findall(f"\\b{given_word}\\b", sentence, re.IGNORECASE)

print(len(match))


import re

sentence = input().lower()
given_word = input().lower()

regex = f"\\b{given_word}\\b"

words = re.findall(regex, sentence)
occurrences = words.count(given_word)

print(occurrences)

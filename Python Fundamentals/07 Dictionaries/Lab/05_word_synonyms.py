n = int(input())

synonyms_dictionary = {}

for i in range(n):
    word = input()
    synonym = input()

    if word not in synonyms_dictionary:
        synonyms_dictionary[word] = []
        synonyms_dictionary[word].append(synonym)
    else:
        synonyms_dictionary[word].append(synonym)

for word, synonym in synonyms_dictionary.items():
    print(f"{word} - {', '.join(synonym)}")

text = input()

char_counter = {}

for ch in text:
    if ch not in char_counter:
        char_counter[ch] = 1
    else:
        char_counter[ch] += 1

char_counter = dict(sorted(char_counter.items(), key=lambda x: x[0]))

for key, value in char_counter.items():
    print(f"{key}: {value} time/s")

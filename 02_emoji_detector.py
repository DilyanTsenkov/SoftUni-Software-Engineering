import re


def threshold(input_string):
    c_threshold = 1
    digit_regex = r"[0-9]"
    digits = re.findall(digit_regex, input_string)
    for digit in digits:
        c_threshold *= int(digit)
    return c_threshold


def emoji_checker(input_string, cool):
    all_of_emojis = []
    cool_of_emojis = []
    emoji_regex = r"(?P<symbols>\:\:|\*\*)(?P<emoji>[A-Z][a-z][a-z]+)(?P=symbols)"
    emojis = re.finditer(emoji_regex, input_string)
    for data in emojis:
        coolness = 0
        d = data.groupdict()
        for char in d["emoji"]:
            coolness += ord(char)
        emoji_found = d["symbols"] + d["emoji"] + d["symbols"]
        all_of_emojis.append(emoji_found)
        if coolness > cool:
            cool_of_emojis.append(emoji_found)
    return all_of_emojis, cool_of_emojis


string = input()

cool_threshold = threshold(string)
all_emojis, cool_emojis = emoji_checker(string, cool_threshold)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(all_emojis)} emojis found in the text. The cool ones are:")
cool_emojis = [print(_, end="\n") for _ in cool_emojis]

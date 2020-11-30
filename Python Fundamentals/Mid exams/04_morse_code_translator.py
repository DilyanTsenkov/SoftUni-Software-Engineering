morse_code_dict = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..'}

message = input().split(" | ")
translated_message = ""

for i in range(len(message)):
    word = message[i].strip()
    word = word.split()
    for letter in word:
        for key, value in morse_code_dict.items():
            if value == letter:
                translated_message += key
                break
    translated_message += " "

print(translated_message.strip())

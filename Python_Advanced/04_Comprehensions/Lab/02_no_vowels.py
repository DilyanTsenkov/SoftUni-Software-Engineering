string = input()

vowels = ['a', 'o', 'u', 'e', 'i']
[vowels.append(el.upper()) for el in list(vowels)]
string = [char for char in string if char not in vowels]

print("".join(string))

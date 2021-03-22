def vowel_filter(func):
    def wrapper():
        text = func()
        vowels = ["a", "e", "i", "o", "u"]
        result = [letter for letter in text if letter.lower() in vowels]
        return result
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())

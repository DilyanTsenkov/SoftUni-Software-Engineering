class vowels:
    VOWELS = ["A", "a", "E", "e", "I", "i", 'U', 'u', 'Y', 'y', 'O', 'o']

    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.string):
            raise StopIteration
        current_char = self.string[self.index]
        self.index += 1
        if current_char not in vowels.VOWELS:
            return self.__next__()
        return current_char


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration
        if self.counter == len(self.sequence) - 1:
            self.counter = -1
        self.number -= 1
        self.counter += 1
        return self.sequence[self.counter]


result = sequence_repeat('abc', 10)
for item in result:
    print(item, end='')

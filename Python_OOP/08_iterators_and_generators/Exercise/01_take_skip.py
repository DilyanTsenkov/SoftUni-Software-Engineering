class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.first_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        self.count -= 1
        next_number = self.first_number
        self.first_number += self.step
        return next_number


numbers = take_skip(10, 5)
for number in numbers:
    print(number)


def solution():
    def integers():
        current_number = 0
        while True:
            current_number += 1
            yield current_number

    def halves():
        for i in integers():
            current_number = i / 2
            yield current_number

    def take(n, seq):
        result = []
        for el in range(0, n):
            result.append(next(seq))
        return result

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

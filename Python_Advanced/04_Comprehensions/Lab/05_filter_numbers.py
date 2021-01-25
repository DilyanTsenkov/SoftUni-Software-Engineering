start = int(input())
end = int(input())

numbers = [i for i in range(start, end + 1) for x in range(2, 11) if i % x == 0]
numbers = set(numbers)

print(list(numbers))

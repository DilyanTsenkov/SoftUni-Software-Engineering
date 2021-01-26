numbers = [int(n) for n in input().split(", ")]

positive = [str(number) for number in numbers if number >= 0]
negative = [str(number) for number in numbers if number < 0]
even = [str(number) for number in numbers if number % 2 == 0]
odd = [str(number) for number in numbers if number % 2 != 0]

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")

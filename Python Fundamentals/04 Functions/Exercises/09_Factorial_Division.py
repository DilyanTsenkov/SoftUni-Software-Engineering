def factorial(num1, num2):
    first_factorial = first_number
    second_factorial = second_number
    for i in range(1, num1):
        first_factorial *= (first_number - i)
    for i in range(1, num2):
        second_factorial *= (second_number - i)
    return first_factorial / second_factorial


first_number = int(input())
second_number = int(input())

print(f"{(factorial(first_number, second_number)):.2f}")

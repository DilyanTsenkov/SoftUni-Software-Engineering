def multiplication(first_number, second_number, third_number):
    if first_number == 0 or second_number == 0 or third_number == 0:
        return "zero"
    elif (first_number < 0 and second_number < 0 and third_number > 0) or (
            first_number < 0 and second_number > 0 and third_number < 0) or (
            first_number > 0 and second_number < 0 and third_number < 0) or (
            first_number > 0 and second_number > 0 and third_number > 0):
        return "positive "
    else:
        return "negative"


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(multiplication(num1, num2, num3))

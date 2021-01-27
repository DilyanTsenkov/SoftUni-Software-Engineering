def absolute(negative_sum):
    return abs(negative_sum)


def compare_negative_positive_sum(negative_sum, positive_sum):
    if positive_sum >= negative_sum:
        return True
    else:
        return False


def negative_separator(numbers):
    if numbers < 0:
        return True


def positive_separator(number):
    if number >= 0:
        return True


def printer(true_ot_false, positive_sum, negative_sum):
    print(negative_sum)
    print(positive_sum)
    if true_ot_false:
        print(f"The positives are stronger than the negatives")
    else:
        print(f"The negatives are stronger than the positives")


def sum_calc(nums):
    return sum(nums)


numbers = [int(el) for el in input().split()]
negative = list(filter(negative_separator, numbers))
positive = list(filter(positive_separator, numbers))
negative_sum = sum_calc(negative)
positive_sum = sum_calc(positive)
negative_abs_sum = absolute(negative_sum)
printer(compare_negative_positive_sum(negative_abs_sum, positive_sum), positive_sum, negative_sum)

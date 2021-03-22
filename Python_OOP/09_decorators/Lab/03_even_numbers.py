import functools


def even_numbers(func):
    @functools.wraps(func)
    def wrapper(numbers):
        n = func(numbers)
        even = [num for num in n if num % 2 == 0]
        return even

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))

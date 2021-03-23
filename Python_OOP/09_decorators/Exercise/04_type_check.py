import functools


def type_check(check_type):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(receive):
            if type(receive) != check_type:
                return "Bad Type"
            return func(receive)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

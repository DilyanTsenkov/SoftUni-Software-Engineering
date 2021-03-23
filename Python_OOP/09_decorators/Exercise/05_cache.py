import functools


def cache(func):
    @functools.wraps(func)
    def wrapper(num):
        result = func(num)
        wrapper.log[num] = result
        return result

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)

fibonacci(5)
print(fibonacci.log)

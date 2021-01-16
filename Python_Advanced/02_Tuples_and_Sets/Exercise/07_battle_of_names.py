def odd_even_checker(n_fun):
    even_fun = set()
    odd_fun = set()
    for number in range(1, n_fun + 1):
        name = input()
        ascii_sum = 0
        for ch in name:
            ascii_sum += ord(ch)
        result = ascii_sum // number
        if result % 2 == 0:
            even_fun.add(result)
        else:
            odd_fun.add(result)
    return odd_fun, even_fun


def sum_odd_even(odd_fun, even_fun):
    odd_sum_fun = sum(odd_fun)
    even_sum_fun = sum(even_fun)
    return odd_sum_fun, even_sum_fun


def action(odd_fun, even_fun):
    union_fun = odd_fun.union(even_fun)
    different_fun = odd_fun.difference(even_fun)
    symmetric_fun = odd_fun.symmetric_difference(even_fun)
    return union_fun, different_fun, symmetric_fun


def printer(odd_sum_fun, even_sum_fun, union_fun, different_fun, symmetric_fun):
    if odd_sum_fun == even_sum_fun:
        print(*union_fun, sep=", ")
    elif odd_sum_fun > even_sum_fun:
        print(*different_fun, sep=", ")
    else:
        print(*symmetric_fun, sep=", ")


n = int(input())
odd, even = odd_even_checker(n)
odd_sum, even_sum = sum_odd_even(odd, even)
union, different, symmetric = action(odd, even)
printer(odd_sum, even_sum, union, different, symmetric)

def get_primes(numbers):
    for num in numbers:
        flag = False
        if num <= 1:
            flag = True
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
        if not flag:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

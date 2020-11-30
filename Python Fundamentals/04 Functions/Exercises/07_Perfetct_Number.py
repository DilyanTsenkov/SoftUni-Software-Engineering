def perfect_num(parameter):
    iterator = parameter
    sum_divisors = 0
    while True:
        if parameter % 2 == 0:
            parameter = parameter // 2
        else:
            parameter = parameter // 2 + 1
        sum_divisors += parameter
        if parameter <= 1:
            break
    if sum_divisors == iterator:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())

perfect_num(number)



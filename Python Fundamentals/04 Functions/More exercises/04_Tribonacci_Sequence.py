def tribonacci_sequence(number):
    tribonacci_list = [1]
    tribonacci_sum = 1
    tribonacci_last_three = []
    for tribo in range(1, int(num)):
        if tribo > 2:
            tribonacci_sum = sum(tribonacci_list[-3:])
            tribonacci_list.append(tribonacci_sum)
        else:
            tribonacci_sum = sum(tribonacci_list[:3])
            tribonacci_list.append(tribonacci_sum)
    print_string = " ".join(str(n) for n in tribonacci_list)
    return print_string


num = input()

print(tribonacci_sequence(num))

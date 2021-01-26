def absolute_value(receive):
    result = [abs(el) for el in receive]
    return result


receive = [float(el) for el in input().split()]
print(absolute_value(receive))

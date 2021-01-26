def rounding(receive):
    result = [round(el) for el in receive]
    return result


receive = [float(el) for el in input().split()]
print(rounding(receive))

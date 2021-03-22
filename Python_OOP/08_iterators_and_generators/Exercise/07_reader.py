def read_next(*args):
    for arg in args:
        try:
            for i in range(len(arg)):
                yield arg[i]
        except:
            for k in arg.keys():
                yield k


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}, "abv", ["z", "k", "l", 1]):
    print(item, end='')

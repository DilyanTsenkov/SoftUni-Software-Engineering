targets = list(map(int, input().split()))

while True:
    index = input()

    if index == "End":
        break

    index = int(index)

    if index in range(len(targets)):
        reduce = targets.pop(index)

        for target in range(len(targets)):
            if targets[target] != -1:
                if reduce < targets[target]:
                    targets[target] -= reduce
                else:
                    targets[target] += reduce

        targets.insert(index, -1)

counter = targets.count(-1)
targets = [str(target) for target in targets]

print(f'Shot targets: {counter} -> {" ".join(targets)}')

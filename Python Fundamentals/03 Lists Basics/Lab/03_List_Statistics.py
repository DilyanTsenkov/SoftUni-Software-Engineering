number = int(input())

positive_list = []
negative_list = []

for num in range(number):
    integer = int(input())
    if integer < 0:
        negative_list.append(integer)
    else:
        positive_list.append(integer)

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}. Sum of negatives: {sum(negative_list)}")

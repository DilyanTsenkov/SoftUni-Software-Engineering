number = int(input())
word = input()

my_list = []
word_list = []

for line in range(number):
    string_input = input()
    my_list.append(string_input)

for i in range(len(my_list)):
    if word in my_list[i]:
        word_list.append(my_list[i])

print(my_list)
print(word_list)

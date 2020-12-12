def create(string):
    my_dict = {}
    pairs = string.split(" | ")
    for pair in pairs:
        pair = pair.split(": ")
        word = pair[0]
        definition = pair[1]
        if word not in my_dict:
            my_dict[word] = [definition]
        else:
            my_dict[word].append(definition)
    return my_dict


def checker(my_dict, input_words):
    words = input_words.split(" | ")
    for word in words:
        if word in my_dict:
            print(f"{word}:")
            def_list = my_dict[word]
            def_list.sort(key=len, reverse=True)
            for n in def_list:
                print(f"-{n}")


def end(my_dict, command):
    if command == "End":
        exit()
    elif command == "List":
        my_dict = dict(sorted(my_dict.items(), key=lambda x: x[0]))
        to_print = ""
        for key in my_dict:
            to_print += f"{key} "
        to_print = to_print.strip()
        print(to_print)


input_string = input()
words = input()
command = input()

my_dict = create(input_string)
checker(my_dict, words)
end(my_dict, command)

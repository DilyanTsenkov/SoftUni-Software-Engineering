def age_assignment(*args, **kwargs):
    dict_to_print = {}
    for name in args:
        for key, value in kwargs.items():
            if name[0] == key:
                dict_to_print[name] = value
    return dict_to_print


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

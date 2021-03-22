class dictionary_iter:
    def __init__(self, dict_object):
        self.dict_object = dict_object
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == len(self.dict_object) - 1:
            raise StopIteration
        self.counter += 1
        return tuple(iter(self.dict_object.items()))[self.counter]


result = dictionary_iter({1: "1", 2: "2"})

for x in result:
    print(x)

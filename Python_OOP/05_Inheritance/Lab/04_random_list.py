import random


class RandomList(list):
    def get_random_element(self):
        el = random.choice(self)
        self.remove(el)
        return el

# class RandomList(list):
#     def get_random_element(self):
#         element_i = random.randint(0, len(self) - 1)
#         element = self[element_i]
#         self.pop(element_i)
#         return element

# Easy way-----------------------------------
# class reverse_iter:
#     def __init__(self, iterable):
#         self.iterable = iterable
#
#     def __iter__(self):
#         return reversed(self.iterable)

# Normal way------------------------------------
class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        if not self.iterable:
            raise StopIteration
        current = self.iterable.pop()
        return current

# hard way---------------------------------------
# class reverse_iter:
#     def __init__(self, iterable):
#         self.iterable = iterable
#
#     def __iter__(self):
#         return self.iterator(self)
#
#     class iterator:
#         def __init__(self, reversed_iter_obj):
#             self.iter = list(reversed_iter_obj.iterable)
#
#         def __iter__(self):
#             return self
#
#         def __next__(self):
#             if not self.iter:
#                 raise StopIteration
#             current = self.iter.pop()
#             return current


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)


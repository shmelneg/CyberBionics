class ReverseIterator:

    def __init__(self, origin):
        self.back_origin = origin[::-1]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.back_origin):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.back_origin[index]


test_list = ['one', 'two', 'three', 'four', 'five', 'six']

modified_iterator = ReverseIterator(test_list)

for item in modified_iterator:
    print(item)

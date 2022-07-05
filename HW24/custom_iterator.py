class DictMap:
    class DictMapIter:
        def __init__(self, iterable):
            self.iterable = iterable
            self.pointer = 0

        def __next__(self):
            if self.pointer == len(self.iterable.items):
                raise StopIteration()
            key_result = self.iterable.key_function(self.iterable.items[self.pointer][0])
            value_result = self.iterable.value_function(self.iterable.items[self.pointer][1])
            self.pointer += 1
            return {key_result: value_result}

    def __init__(self, records, key_function, value_function):
        self.items = tuple(records.items())
        self.key_function = key_function
        self.value_function = value_function

    def __iter__(self):
        return self.DictMapIter(self)


def add_two(key):
    return key + 2


dictionary = {1: 5, 2: 6, 3: 7, 4: 8}

s = DictMap(dictionary, add_two, str)
for i in s:
    print(i)

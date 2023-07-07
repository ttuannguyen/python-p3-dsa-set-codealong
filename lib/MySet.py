class MySet:

    # we are operating on the underlying Dictionary data structure
    def __init__(self, enumerable = []):
        # print(self)
        # print(enumerable)
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

    def size(self):
        # print(len(self.dictionary))
        return len(self.dictionary)


set = MySet([1,2,3,3,4,4])
set.has(4)
set.size()
print(set.dictionary)


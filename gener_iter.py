class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.counter = -1

    def __iter__(self):
        # Выполняется на входе в цикл
        self.counter +=1
        self.nest_cursor = 0
        return self

    def __next__(self):
        # Выполняется на каждой итерации цикла
        if self.nest_cursor >= len(self.list_of_list[self.counter]):
           iter(self)
        if self.counter >= len(self.list_of_list):  # Условие завершения цикла
            raise StopIteration

        item = self.list_of_list[self.counter][self.nest_cursor]
        self.nest_cursor += 1

        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for elem in FlatIterator(list_of_lists_1):
        print(elem)

    test_1()

import types
import itertools


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.index_list = 0
        self.item_list = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index_list >= len(self.list_of_list):
            raise StopIteration
        elif self.item_list >= len(self.list_of_list[self.index_list]):
            self.index_list += 1
            self.item_list = 0
            return self.__next__()
        item = self.list_of_list[self.index_list][self.item_list]
        self.item_list += 1
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

list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]


def flat_generator(list_of_lists):
    flat_list = list(itertools.chain.from_iterable(list_of_lists))
    for i in flat_list:
        yield i


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
if __name__ == '__main__':
    test_1()
    test_2()
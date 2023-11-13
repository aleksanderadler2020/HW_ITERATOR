def flat_list(arr):
    res = []
    for obj in arr:
        res += flat_list(obj) if isinstance(obj, list) else [obj]
    return res


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = flat_list(list_of_list)
        self.start = 0
        self.end = len(self.list_of_list)

    def __iter__(self):
        self.current_value = self.start
        return self

    def __next__(self):
        cur_val = self.current_value
        self.current_value += 1
        if self.current_value > self.end:
            raise StopIteration
        return self.list_of_list[cur_val]


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()

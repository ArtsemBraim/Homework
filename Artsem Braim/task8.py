class MySquareIterator:

    def __init__(self, col):
        self._col = col
        self._current_idx = 0
        self._len = len(col)

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_idx < self._len:
            self._current_idx += 1
            return self._col[self._current_idx - 1] ** 2
        else:
            raise StopIteration


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item, end=" ")

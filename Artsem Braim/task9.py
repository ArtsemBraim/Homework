class EvenRange:

    def __init__(self, start, end):
        self._start = start
        self._end = end
        if start % 2 == 0:
            self._current = start
        else:
            self._current = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._current < self._end:
            self._current += 2
            return self._current - 2
        else:
            print("Out if numbers")
            raise StopIteration


if __name__ == "__main__":
    er1 = EvenRange(7, 11)
    print(next(er1))
    print(next(er1))
    print(next(er1))
    print(next(er1))
    er2 = EvenRange(3, 14)
    for number in er2:
        print(number, end=" ")

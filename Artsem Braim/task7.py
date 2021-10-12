class MyNumberCollection:
    def __init__(self, *args):
        self.__coll = []
        if len(args) == 1:
            tmp_coll = list(*args)
            for i in tmp_coll:
                if isinstance(i, (int, float)):
                    self.__coll.append(i)
                else:
                    raise TypeError("MyNumberCollection supports only numbers!")

        else:
            self.__coll = list(range(args[0], args[1], args[2]))
            if args[1] not in self.__coll:
                self.__coll.append(args[1])

    def append(self, item):
        if isinstance(item, (int, float)):
            self.__coll.append(item)
        else:
            raise TypeError(f"{item!r} - object is not a number!")

    def __add__(self, other):
        return MyNumberCollection(self.__coll + other.__coll)

    def __getitem__(self, item):
        return self.__coll[item] ** 2

    def __iter__(self):
        self._idx = -1
        return self

    def __next__(self):
        self._idx += 1
        if self._idx < len(self.__coll):
            return self.__coll[self._idx]
        else:
            raise StopIteration

    def __str__(self):
        return str(self.__coll)


if __name__ == "__main__":
    col1 = MyNumberCollection(0, 5, 2)
    print(col1)
    col2 = MyNumberCollection((1, 2, 3, 4, 5))
    print(col2)
    # col3 = MyNumberCollection([1, 2, 3, "4", 5])
    col1.append(7)
    print(col1)
    # col2.append("string")
    print(col1 + col2)
    print(col1)
    print(col2)
    print(col2[4])
    for item in col1:
        print(item)


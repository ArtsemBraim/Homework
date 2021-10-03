class Counter:

    def __init__(self, start=0, stop=None):
        self.value = start
        self.stop = stop

    def increment(self):
        try:
            if self.stop is None or self.value < self.stop:
                self.value += 1
            else:
                raise OverflowError("Maximum value is reached")
        except OverflowError as e:
            print(e)

    def get(self):
        return self.value


if __name__ == "__main__":
    c = Counter(start=42)
    c.increment()
    print(c.get())

    c = Counter()
    c.increment()
    print(c.get())
    c.increment()
    print(c.get())

    c = Counter(start=42, stop=43)
    c.increment()
    print(c.get())
    c.increment()
    print(c.get())

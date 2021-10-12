import time


def endless_fib_generator():
    f0 = 0
    f1 = 1
    yield 1
    while True:
        current = f0 + f1
        f0 = f1
        f1 = current
        yield current


if __name__ == "__main__":
    gen = endless_fib_generator()
    while True:
        print(next(gen), end=" ")
        time.sleep(0.5)

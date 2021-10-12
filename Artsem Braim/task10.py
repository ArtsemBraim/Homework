import time


def endless_generator():
    i = -1
    while True:
        i += 2
        yield i


if __name__ == "__main__":
    gen = endless_generator()
    while True:
        print(next(gen), end=" ")
        time.sleep(0.5)

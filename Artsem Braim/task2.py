from contextlib import contextmanager


@contextmanager
def open_file(*args, **kwargs):
    try:
        file = open(*args, **kwargs)
    except Exception as exc:
        print(exc)
        file = None

    yield file

    if file is not None:
        file.close()


if __name__ == "__main__":
    with open_file("some_file.txt", "r") as file:
        print(file.read())

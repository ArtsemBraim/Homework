class OpenFile:

    def __init__(self, *args, **kwargs):
        try:
            self._file = open(*args, **kwargs)
        except Exception as exc:
            print(exc)
            self._file = None

    def __enter__(self):
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._file is not None:
            self._file.close()


if __name__ == "__main__":
    with OpenFile("some_file.txt", "r") as file:
        print(file.read())

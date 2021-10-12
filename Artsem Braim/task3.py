import time
from contextlib import ContextDecorator


class ExecutionTime(ContextDecorator):

    def __init__(self, filename):
        self._log_file = open(filename, "w")

    def __enter__(self):
        self._start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._log_file.write(f"Execution time - {time.time() - self._start}")
        self._log_file.close()


@ExecutionTime("logfile.txt")
def print_numbers():
    for i in range(1000):
        print(i)


if __name__ == "__main__":
    print_numbers()
    with ExecutionTime("logfile.txt"):
        for i in range(1000):
            print(i)

def suppress_exception(f):

    def wrapper(*args):
        try:
            f(*args)
        except Exception as exc:
            print(exc)
        else:
            print("Exceptions have not been caught")

    return wrapper


@suppress_exception
def zero_division():
    a = 1 / 0


@suppress_exception
def func_without_exception():
    a = 1


if __name__ == "__main__":
    zero_division()
    func_without_exception()

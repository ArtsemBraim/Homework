def remember_result(f):
    result = None

    def wrapper(*args):
        nonlocal result
        print(f"Last result = '{result}'")
        result = f(*args)

    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    if len(args) != 0 and isinstance(args[0], int):
        result = 0
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result


if __name__ == "__main__":
    sum_list("a", "b")
    sum_list("abc", "cde")
    sum_list(3, 4, 5)

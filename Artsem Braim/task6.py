def call_once(f):
    result = None

    def wrapper(a, b):
        nonlocal result
        if result is None:
            result = f(a, b)
        return result

    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


if __name__ == "__main__":
    print(sum_of_numbers(13, 42))
    print(sum_of_numbers(999, 100))
    print(sum_of_numbers(134, 412))
    print(sum_of_numbers(856, 232))

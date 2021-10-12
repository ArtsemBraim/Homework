class NotEvenError(ValueError):
    pass


class LessThanTwoError(ValueError):
    pass


def check_number(number):
    if number % 2 != 0:
        raise NotEvenError("Number is not even")
    elif number < 2:
        raise LessThanTwoError("Number is less than two ")


if __name__ == "__main__":
    check_number(4)
    check_number(3)

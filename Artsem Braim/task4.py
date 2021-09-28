a = "I am global variable!"


def enclosing_function():
    a = "I am variable from enclosed function!"

    def inner_function():
        global a
        print(a)

    return inner_function


def enclosing_function2():
    a = "I am variable from enclosed function!"

    def inner_function():
        nonlocal a
        print(a)

    return inner_function


caller = enclosing_function()
caller()


caller = enclosing_function2()
caller()

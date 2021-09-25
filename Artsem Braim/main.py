import math
import re
import string


# task1
def switch_quotes(s):
    return s.replace('\'', '_').replace('"', '\'').replace('_', '"')


# task2
def is_palindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False

    return True


# task3
def split(s, sep=None, maxsplit=-1):
    splitted = []
    prev_index = 0
    if sep is None:
        start = None
        for i in range(len(s)):
            if s[i].isspace():
                if start is not None:
                    splitted.append(s[start:i])
                    start = None
                    maxsplit -= 1
            else:
                if maxsplit == 0:
                    splitted.append(s[i:-1])
                    break
                if start is None:
                    start = i
    else:
        while True:
            index = s.find(sep, prev_index)
            if index == -1 or maxsplit == 0:
                splitted.append(s[prev_index:])
                break
            else:
                splitted.append(s[prev_index:index])
                prev_index = index + len(sep)
            maxsplit -= 1

    return splitted


# task4
def split_by_index(s, indexes):
    splitted = []
    prev_index = 0
    for index in indexes:
        splitted.append(s[prev_index:index])
        prev_index = index

    return splitted


# task5
def get_digits(number):
    return tuple([int(digit) for digit in str(number)])


# task6
def get_longest_word(s):
    words = re.split(r'\s+', s)

    if len(words) == 1:
        return words[0]
    else:
        max_index = 0
        max_length = len(words[0])

        for i in range(1, len(words)):
            if max_length < len(words[i]):
                max_index = i
                max_length = len(words[i])

    return words[max_index]


# task7
def foo(lst):
    product = math.prod(lst)
    new_lst = []
    for item in lst:
        new_lst.append(int(product / item))

    return new_lst


# task8
def get_pairs(lst):
    if len(lst) == 1:
        return None
    else:
        pairs = []

        for i in range(1, len(lst)):
            pairs.append((lst[i - 1], lst[i]))

    return pairs


# task9.1
def test_1_1(*args):
    chars = set()
    is_first_iteration = True
    for word in args:
        if is_first_iteration:
            chars = set(word.lower())
            is_first_iteration = False

        chars &= set(word.lower())

    return chars


# task9.2
def test_1_2(*args):
    chars = set()
    for word in args:
        chars |= set(word.lower())

    return chars


# task9.3
def test_1_3(*args):
    chars = set()
    for i in range(len(args) - 1):
        for ch in args[i].lower():
            if ch not in chars:
                for j in range(i + 1, len(args)):
                    if ch in args[j]:
                        chars.add(ch)

    return chars


# task9.4
def test_1_4(*args):
    alphabet = set(string.ascii_lowercase)

    for word in args:
        alphabet -= set(word.lower())

    return alphabet


# task10
def generate_squares(number):
    return {i: i ** 2 for i in range(1, number + 1)}


# task11
def combine_dicts(*args):
    dicts = dict()
    for dictionary in args:
        for k, v in dictionary.items():
            if k in dicts:
                dicts[k] += v
            else:
                dicts[k] = v

    return dicts

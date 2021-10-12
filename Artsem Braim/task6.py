from task5 import NotEvenError, LessThanTwoError


def find_prime_numbers(num):
    prime_numbers = [1]
    k = 0
    for i in range(2, num):
        for j in range(2, i):
            if i % j == 0:
                k += 1
        if k == 0:
            prime_numbers.append(i)
        else:
            k = 0

    return prime_numbers


def solve_goldbachs_conjecture(num):
    if num % 2 != 0:
        raise NotEvenError
    elif num < 2:
        raise LessThanTwoError
    else:
        prime_numbers = find_prime_numbers(num)
        x = prime_numbers[-1]
        y = -1
        for i in prime_numbers:
            if x + i == num:
                y = i
                break

    return x, y


if __name__ == "__main__":
    print("Enter 'q' to quit")
    while True:
        choice = input("Enter a even number: ")
        if choice == "q":
            break
        else:
            try:
                if choice.isdigit():
                    print(solve_goldbachs_conjecture(int(choice)))
                else:
                    print("It is not a number. Try again!")
            except NotEvenError:
                print("It is not an even number. Try again!")
            except LessThanTwoError:
                print("It is less than 2. Try again!")


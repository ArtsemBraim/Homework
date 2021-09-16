number = 60

divisors = set()
i = 1
stop_value = number ** 0.5
while i <= stop_value:
    if number % i == 0:
        divisors.add(i)
        divisors.add(int(number / i))
    i += 1

print(sorted(divisors))

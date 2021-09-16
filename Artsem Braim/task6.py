tpl = 1, 2, 3, 4

str_tpl = [str(item) for item in tpl]

number = int(''.join(str_tpl))

print(number)

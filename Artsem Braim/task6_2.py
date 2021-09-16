a = 2
b = 4
c = 3
d = 7

print(' ', end='\t')
for i in range(c, d + 1):
    print(i, end='\t')
for i in range(a, b + 1):
    print('\n' + str(i), end='\t')
    for j in range(c, d + 1):
        print(i * j, end='\t')

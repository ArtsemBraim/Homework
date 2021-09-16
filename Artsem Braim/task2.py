input_str = 'Oh, it is python'

frequency = {}
for char in input_str.lower():
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)

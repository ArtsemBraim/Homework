my_dict = {4: 1, 19: 5, 5: 3, 10: 7, -5: 2}

sorted_dict = {key: my_dict[key] for key in sorted(my_dict)}

print(sorted_dict)

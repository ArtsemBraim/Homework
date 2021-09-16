my_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
           {"VIII": "S007"}]

values = []
for item in my_dict:
    values += list(item.values())

unique_values = set(values)

print(unique_values)

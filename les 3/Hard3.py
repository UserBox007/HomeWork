def calculate_structure_sum(data_structure):
    result = 0
    if isinstance(data_structure, int):
        result += data_structure
    elif isinstance(data_structure, str):
        result += len(data_structure)
    else:
        for val in data_structure:
            if isinstance(data_structure, dict):
                result += calculate_structure_sum(data_structure[val])
            if isinstance(val, int):
                result += val
            elif isinstance(val, str):
                result += len(val)
            else:
                result += calculate_structure_sum(val)

    return result



data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)



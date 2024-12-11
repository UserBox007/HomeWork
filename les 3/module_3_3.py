def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [11,"dmmada", (4,2)]
values_dict = {"a" :"s", "b":22, "c":values_list}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
print_params(42, *values_list_2)
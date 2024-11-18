immutable_var = (1, 'dsdsds', 4, (3,4))
print(immutable_var)

# immutable_var[1] = 'www'
# TypeError: 'tuple' object does not support item assignment

mutable_list = [2,4,4,'sqsqs',2]
print(f'Оригинальный лист {mutable_list}')

mutable_list[1] = '3'
mutable_list[3] = 'ДругойЭлемент'
print(f'Результат замены {mutable_list}')
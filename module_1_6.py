# Работа со словарями:

my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict["Egor"]}')
print(f'Not existing value: {my_dict.get("Fedor")}')
my_dict['Petya'] = 1986
my_dict['Slava'] = 1988
print(f'New dict: {my_dict}')
del_item = my_dict.pop("Egor")
print(f'Del item: {del_item}')
print(f'Finally dict: {my_dict}')

#Работа с множествами:

my_set  = {1,1,1,'Vasya', 1975, 'Egor', 1999, 'Masha', 2002, 'Masha'}
print(f'Set: {my_set}')
my_set.add('NewElement')
my_set.add((1,2,3))
my_set.discard(1)
print(f'Set: {my_set}')
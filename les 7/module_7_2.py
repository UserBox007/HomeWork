def  custom_write(file_name, strings):
    text = ''
    number = 0
    pos = 0
    result = {}
    file = open(file_name, 'w', encoding='utf-8')

    for string in strings:
        pos = file.tell()
        number += 1
        text =  string + '\n'
        file.write(text)

        result[(number, pos)] = string


    file.close()
    return result


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]



result = custom_write('test.txt', info)

for elem in result.items():
  print(elem)

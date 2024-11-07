def custom_write(file_name, strings):
    str_num = 0
    pos = 0
    items = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for string in strings:
            pos = file.tell()
            str_num += 1
            file.write(string)
            file.write('\n')
            items.update({(str_num, pos): string})
    file.close()
    return items


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

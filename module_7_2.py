def custom_write(file_name, strings):
    strings_positions = {}
    number_str = 0
    file = open(file_name, 'a+', encoding='utf-8')
    for string in strings:
        number_str += 1
        key = number_str, file.tell()
        file.write(f'{string}\n')
        strings_positions[key] = string
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
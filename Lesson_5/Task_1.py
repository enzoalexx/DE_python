# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.


with open('2342.txt', 'w+', encoding='utf-8') as f_obj:
    line = input('Введите текст - ')
    while line:
        f_obj.write(line)
        line = input('Введите текст - ')
        f_obj.write('\n')
        if not line:
            break
with open('2342.txt', encoding='utf-8') as f_obj:
    lines = f_obj.readlines()
    print(lines)
    for line in lines:
        print(line, end='')

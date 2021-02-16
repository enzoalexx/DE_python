# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.


numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять', 'Six': 'Шесть',
           'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Ten': 'Десять'}
new_elem = []
with open('Task_4.txt', 'r') as f_obj:
    lines = f_obj.readlines()
    for line in lines:
        line = line.split(' ', 1)
        new_elem.append(numbers[line[0]] + '  ' + line[1])
    print(new_elem)
with open('Task_4_new.txt', 'w+') as f_obj_2:
    f_obj_2.writelines(new_elem)

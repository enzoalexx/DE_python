# Создать текстовый файл (не программно), сохранить в нём
# несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open('Task_2.txt', encoding='utf-8') as f_obj:
    lines = f_obj.readlines()
    print(lines)
    count = 0
    for line in lines:
        print(f'{line.strip()} // Количество слов в строке - {line.count(" ") + 1}')
        count += 1
    print(f'Количество строк в файле - {count}')

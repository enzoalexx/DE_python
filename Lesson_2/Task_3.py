# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

season_list = ['winter', 'spring', 'summer', 'autumn']
season_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
month = int(input('Введите цифру месяца '))
if month == 12 or 1 == month == 2:
    print(season_list[0])
    print(season_dict.get(1))
if 3 <= month <= 5:
    print(season_list[1])
    print(season_dict.get(2))
if 6 <= month <= 8:
    print(season_list[2])
    print(season_dict.get(3))
if 9 <= month <= 11:
    print(season_list[3])
    print(season_dict.get(4))
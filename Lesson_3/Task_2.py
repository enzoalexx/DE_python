# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def my_func(name: str, surname: str, birth_year: int, city: str, email: str, phone: int):
    print(name, surname, birth_year, city, email, phone)


my_func(name=input('Введите имя - '), surname=input('Введите фамилию - '),
        birth_year=int(input('Введите год рождения - ')), city=input('Введите город проживания - '),
        email=input('Введите email - '), phone=int(input('Введите номер телефона - ')))

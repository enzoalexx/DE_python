# 3. Реализовать функцию my_func(), которая принимает три
# позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(arg1: int, arg2: int, arg3: int):
    if arg1 >= arg3 and arg2 >= arg3:
        print(arg1 + arg2)
    elif arg1 > arg2 and arg3 > arg2:
        print(arg1 + arg3)
    else:
        print(arg2 + arg3)


my_func(arg1=(int(input('Введите первый аргумент - '))),
        arg2=(int(input('Введите второй агрумент - '))),
        arg3=(int(input('Введите третий аргумент - '))))

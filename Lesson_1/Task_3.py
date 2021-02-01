# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

# с помощью переменных для конкретного условия n + nn + nnn
n = (input('Введите число n - '))
temp1 = int(2 * n)
temp2 = int(3 * n)
print(f'{int(n)} + {temp1} + {temp2} = {int(n) + temp1 + temp2}')

# с помощью цикла for для n + nn + nnn + ... + nnnn - n раз
n = (input('Введите число n - '))
temp = 0
for i in range(1, int(n) + 1):
    temp += int(i * str(n))
    print(i * str(n))
print()
print(temp)
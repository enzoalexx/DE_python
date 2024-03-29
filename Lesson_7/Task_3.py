# 3. Реализовать программу работы с клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству
# клеток (целое число). В классе должны быть реализованы методы перегрузки
# арифметических операторов:
# сложение (add()),
# вычитание (sub()),
# умножение (mul()),
# деление (truediv()).
# Данные методы должны выполнять увеличение,уменьшение, умножение и
# обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# В классе необходимо реализовать метод make_cell(), принимающий экземпляр класса
# и количество клеток в ряду. Метод должен возвращать строку вида **\n\n**...,
# где количество клеток между \n равно переданному аргументу, а количество рядов
# определяется, исходя из общего количества клеток.
# При создании экземпляра клетки должна происходить перезапись параметра,
# который хранит количество клеток.

class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_cell(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return 'Sum of cell is ' + str(self.nums + other.nums)

    def __sub__(self, other):
        return 'Subtraction of cell is ' + str(self.nums - other.nums) if self.nums - other.nums > 0 \
            else 'Ячеек в первой клетке меньше или равно второй, вычитание невозможно'

    def __mul__(self, other):
        return 'Multiply of cells is ' + str(self.nums * other.nums)

    def __truediv__(self, other):
        return 'Truediv of cells is ' + str(round(self.nums / other.nums))


cell_1 = Cell(10)
cell_2 = Cell(8)
print(cell_1)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_cell(4))

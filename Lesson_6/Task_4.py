# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
# выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} поехал со скоростью {self.speed}')

    def stop(self):
        return f'Автомобиль {self.name} остановился'

    def turn_right(self):
        return f'Автомобиль {self.name} повернул направо'

    def turn_left(self):
        return f'Автомобиль {self.name} повернул налево'

    def show_speed(self):
        return f'Автомобиль {self.name} едет со скоростью {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Городской автомобиль {self.name} едет со скоростью {self.speed}')

        if self.speed > 60:
            return f'Скорость автомобиля больше разрешенной скорости'
        else:
            return f'Скорость автомобиля в пределах нормы'


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Грузовой автомобиль {self.name} едет со скоростью {self.speed}')

        if self.speed > 40:
            return f'Скорость автомобиля больше разрешенной скорости'
        else:
            return f'Скорость автомобиля в пределах нормы'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return self.is_police
        else:
            return self.is_police


mers = SportCar(130, 'Черный', 'Mercedes', False)
smart = TownCar(30, 'Зеленый', 'Smart', False)
scania = WorkCar(70, 'Белый', 'Scania', False)
porsche = PoliceCar(80, 'Голубой',  'Porsche Cayenne', True)
print(scania.turn_left())
print(f'{smart.turn_right()}, затем {mers.stop()}')
scania.go()
print(f'{scania.show_speed()}')
print(f'Цвет {scania.name} - {scania.color}')
print(f'{mers.name} полицейский автомобиль? {mers.is_police}')
print(f'{porsche.name} полицейский автомобиль? {porsche.is_police}')
print(mers.show_speed())
print(smart.show_speed())
print(porsche.police())
print(porsche.show_speed())

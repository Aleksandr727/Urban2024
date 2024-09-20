import math

class Figure:
    sides_count = 0
    def __init__(self, color:tuple[int, int, int], *sides, filled = True):
        self.__color = color
        self.filled = filled
        self.__sides = sides

    def get_color(self):
        return (self.__color)

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    @staticmethod
    def __is_valid_sides(*args):
        for side in args:
            if len(new_sides) != self.sides_count:
                return False
            if not isinstance(side, int) or side <=0:
                return False
        return True

    def get_sides(self):
        return (self.__sides)

    def __len__(self):
        p = 0
        for i in self.get_sides():
            p += i
        return p

    def set_sides(self, *new_sides: int):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, sides):
        super().__init__(color, sides)

        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius**2

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, sides):
        super().__init__(color, sides)

    def get_square(self):
        P = 0
        for i in self.get_sides():
            P += i
        p = P/2
        return ((p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))**0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color: list, *sides: int):
        super().__init__(color, *sides)
self.set_sides(*list(sides) * 12)

    def get_volume(self):
        return self.get_sides()[0]**3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
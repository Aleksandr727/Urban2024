class House:
    def __init__(self, name, floor):
        self.name = name
        self.number_of_floors = floor

    def go_to(self, new_floor):
        print(self.name)
        if new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Университетский', 5)
h2 = House('ЖК Победа', 10)
h1.go_to(5)
h2.go_to(11)


# Второй вариант, посложнее.
class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.number_of_floors_max = number_of_floors

    def go_to(self, new_floor):
        print(self.name)
        if new_floor > self.number_of_floors_max or new_floor < (self.number_of_floors_max-(self.number_of_floors_max-1)):
            print('Такого этажа не существует')
        else:
            self.number_of_floors = new_floor
            print(f'вы в доме {self.name}, на этаже {self.number_of_floors}')

house_1 = House('ЖК Магнус', 30)
house_2 = House('ЖК Тинпик', 5)

print(f'Это дом {house_1.name}, в нем {house_1.number_of_floors} этажей\n')

house_1.go_to(2)
house_1.go_to(22)
house_1.go_to(-2)
house_1.go_to(222)

print(f'Это дом {house_2.name}, в нем {house_2.number_of_floors} этажей\n')
house_2.go_to(1)
house_2.go_to(5)
house_2.go_to(-2)
house_2.go_to(6)


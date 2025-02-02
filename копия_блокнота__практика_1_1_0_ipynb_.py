# -*- coding: utf-8 -*-
"""Копия блокнота "Практика 1.1.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sp5wZPZj2RgZUu-ZDyadj8W1eWhhqsFe

**ФИО:**
"""

Кабанов Данил Алексеевич

"""# Задание 1

**Описание:** Создайте иерархию классов для разных типов сотрудников в компании. Реализуйте родительский класс Employee и дочерние классы Manager и Developer. Каждый класс должен иметь метод для расчета зарплаты на основе различных критериев класса.


Отрабатываемый принцип: Наследование
"""

class Employee:
    def __init__(self, first_name, second_name, job):
        self.first_name = first_name
        self.second_name = second_name
        self.job = job


class Manager(Employee):
    salary_hour = 10000

    def __init__(self, first_name, second_name, job):
        super().__init__(first_name, second_name, job)
        self.salary_job = self.salary_hour

    def get_salary(self):
        return f'Заработная плата менеджера: {self.salary_job} рублей.'


class Developer(Employee):
    salary_hour = 7500

    def __init__(self, first_name, second_name, job):
        super().__init__(first_name, second_name, job)
        self.salary_job = self.salary_hour

    def get_salary(self):
        return f'Заработная плата разработчика: {self.salary_job} рублей.'


people1 = Developer('Oleg', 'Olegov', 'Developer')
people2 = Manager('Ivan', 'Ivanov', 'Manager')
print(people1.get_salary())
print(people2.get_salary())

"""# Задание 2

**Описание:** Создайте иерархию классов для различных типов транспортных средств (Необходим один родительский класс и 3 дочерних). Реализуйте метод, который позволяет каждому транспортному средству возвращать собственное описание (Метод в каждом классе должен иметь одинаковое название). Продемонстрируйте вызов данного метода для каждого транспортного средства.


Отрабатываемый принцип: Полиморфизм
"""

class Transport:
    def __init__(self, all_name, color):
        self.all_name = all_name
        self.color = color


class Tram(Transport):
    def info(self):
        print('Тип транспорта: Трамвай')
        print('Всего сидений: 23')
        print('Всего мест в транспорте: 43\n')


class Bus(Transport):
    def info(self):
        print('Тип транспорта: Автобус')
        print('Всего сидений: 29')
        print('Всего мест в транспорте: 45\n')


class Trolleybus(Transport):
    def info(self):
        print('Тип транспорта: Троллейбус')
        print('Всего сидений: 32')
        print('Всего мест в транспорте: 50')


transp = Tram('Общественный транспорт', 'Красный')
transp2 = Bus('Общественный транспорт', 'Зеленый')
transp3 = Trolleybus('Общественный транспорт', 'Синий')

transp.info()

transp2.info()

transp3.info()

"""# Задание 3

Онлайн-магазин:
- Создайте модель для онлайн-магазина с классами Product, Order, Customer, и ShoppingCart.
- Product включает информацию о цене, наличии на складе и категории товара.
Order обрабатывает процесс покупки, включая расчет цены с учетом скидок и налогов.
- Customer управляет информацией о пользователе и его истории заказов.
- ShoppingCart позволяет добавлять, удалять и обновлять количество товаров перед оформлением заказа.
"""

class Product:
    price_fish = 100
    price_meat = 150

    def __init__(self, category):
        self.category = category
        self.meat = self.price_meat
        self.fish = self.price_fish

    def availability(self):
        if self.category == 'Мясо':
            print(f'Стоимость: {self.meat} руб.')
        elif self.category == 'Рыба':
            print(f'Стоимость: {self.fish} руб.')
        else:
            print('Такого товара нет!')


purchase = Product("Мясо")
purchase.availability()
purchase2 = Product("Рыба")
purchase2.availability()

"""# Задание 4

Симулятор космического корабля:
- Создайте симулятор управления космическим кораблем с классами SpaceShip, CrewMember, и Mission.
- SpaceShip имеет атрибуты для управления топливом, состоянием корпуса, и текущей скоростью.
- CrewMember контролирует здоровье, навыки, и роли в команде (например, пилот, инженер).
- Mission определяет цели, ресурсы, и возможные события (например, аварии, встречи с астероидами).
"""

from random import randint


class SpaceShip:
    def __init__(self, fuel, corps, speed):
        self.fuel = fuel
        self.corps = corps
        self.speed = speed

    def get_fuel(self, fuel_amount):
        self.fuel += fuel_amount
        print(f'Корабль заправлен. Топливо: {self.fuel}')

    def get_state(self, amount):
        self.corps += amount
        print(f'Корабль отремонтирован. Состояние корпуса: {self.corps}')

    def get_speed(self, new_speed):
        self.speed = new_speed
        print(f'Скорость изменена. Текущая скорость: {self.speed}')


class CrewMember:
    def __init__(self, health, skill, role):
        self.health = health
        self.skill = skill
        self.role = role

    def heal(self, amount):
        self.health += amount
        print(f'Член экипажа излечен. Здоровье: {self.health}')

    def use_skill(self):
        print(f'{self.role} использует навык: {self.skill}')


class Mission:
    def __init__(self, goals):
        self.goals = goals
        self.events = []

    def execute_goals(self):
        print('Действия:')
        for goal in self.goals:
            print(f' - {goal}')


spaceship = SpaceShip(100, 80, 0)

pilot = CrewMember(100, 'пилотирование', 'Пилот')
engineer = CrewMember(80, 'ремонт', 'Инженер')

mission = Mission(['Исследовать планету', 'Увеличить скорость', 'Заправиться',\
                   'Починить корабль', 'Узнать статистику корабля',\
                   'Узнать об экипаже', 'Вылечить члена экипажа', 'Закончить'])


while True:
    mission.execute_goals()

    act = input('Введите ваше действие: ')

    if act == 'Исследовать планету':
        if spaceship.speed == 0:
            print('Сначала запустите двигатели!')
        else:
            print('Вы летите на новую планету, которую хотите изучить.')
            print('Вы собрали образцы c этой планеты.')
    elif act == 'Заправиться':
        gas = int(input('Введите, насколько вы хотите заправиться: '))
        spaceship.get_fuel(gas)
    elif act == 'Починить корабль':
        engineer.use_skill()
        repair = randint(10, 50)
        spaceship.get_state(repair)
    elif act == 'Увеличить скорость':
        speed = int(input('Выберите скорость: '))
        spaceship.get_speed(speed)
    elif act == 'Узнать статистику корабля':
        print(f'Топливо: {spaceship.fuel}.')
        print(f'Состояние корабля: {spaceship.corps}.')
        print(f'Скорость: {spaceship.speed}.')
    elif act == 'Узнать об экипаже':
        print(f'Здоровье: {pilot.health}.')
        print(f'Навык: {pilot.skill}.')
        print(f'Роль: {pilot.role}.')
        print('=====================')
        print(f'Здоровье: {engineer.health}.')
        print(f'Навык: {engineer.skill}.')
        print(f'Роль: {engineer.role}.')
    elif act == 'Вылечить члена экипажа':
        healing = randint(20, 45)
        crew = input('Кого вылечите? ')
        if crew == 'pilot':
            pilot.heal(healing)
        elif crew == 'engineer':
            engineer.heal(healing)
    elif act == 'Закончить':
        print('Хорошего дня!')
        break
    else:
        print('Ошибка!')
        break

"""# Дополнительно:

**Описание:** создайте консольную версию игры крестики-нолики, используя классы
"""


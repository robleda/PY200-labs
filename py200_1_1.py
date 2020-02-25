# -*- coding: utf-8

# 
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 1.1 Основы ООП. Понятие класса, объекта. Создание экземпляра класса

# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): Иванов И.И.

# ---------------------------------------------------------------------------------------------
# Понятие класса, объекта (стр. 1-22)

# 1. Создайте класс Glass с атрибутами capacity_volume и occupied_volume
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)


class Glass:
    def __init__(self, capacity_volume, occupied_volume):
        if isinstance(capacity_volume, (int, float)):
            if capacity_volume > 0:
                self.capacity_volume = capacity_volume
            else:
                raise ValueError
        else:
            raise TypeError

        if isinstance(occupied_volume, (int, float)):
            if occupied_volume >= 0:
                self.occupied_volume = occupied_volume
            else:
                raise ValueError
        else:
            raise TypeError


# 2. Создайте два и более объектов типа Glass
#    Измените и добавьте в любой стакан любое кол-во воды (через атрибуты)
#    Убедитесь, что у других объектов Glass атрибуты экземпляра класса не изменились.


glass1 = Glass(200, 100)
# print(glass1.capacity_volume)
# print(glass1.occupied_volume)

glass2 = Glass(300, 150)


# print(glass2.capacity_volume)
# print(glass2.occupied_volume)


# 3. Создайте класс GlassDefaultArg (нужен только __init__) c аргументом occupied_volume
#    По умолчанию occupied_volume равен нулю. Создайте два объекта с 0 и 200
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)


class GlassDefaultArg:
    def __init__(self, capacity_volume, occupied_volume=0):

        if isinstance(capacity_volume, (int, float)):
            if capacity_volume > 0:
                self.capacity_volume = capacity_volume
            else:
                raise ValueError
        else:
            raise TypeError

        if isinstance(occupied_volume, (int, float)):
            if occupied_volume >= 0:
                self.occupied_volume = occupied_volume
            else:
                raise ValueError
        else:
            raise TypeError


glass_3_1 = GlassDefaultArg(200)
# print(glass_3_1.occupied_volume)
glass_3_2 = GlassDefaultArg(200, 200)


# print(glass_3_2.occupied_volume)

# 4. Создайте класс GlassDefaultListArg (нужен только __init__) 
#    c аргументами capacity_volume, occupied_volume.
#    Пусть аргументом по умолчанию для __init__ occupied_volume = []. Будет список.
#    Попробуйте создать 3 объекта, которые изменяют occupied_volume.append(2) внутри __init__.
#    Создавайте объект GlassDefaultListArg только с одним аргументом capacity_volume.
#    Опишите результат.
#    Подсказка: можно ли использовать для аргументов по умолчанию изменяемые типы?


class GlassDefaultListArg:
    def __init__(self, capacity_volume, occupied_volume=[]):
        self.occupied_volume = occupied_volume
        self.occupied_volume.append(2)


glass_4_1 = GlassDefaultListArg(200)
# print(dir(glass_4_1))
# print(glass_4_1.__dict__)
glass_4_2 = GlassDefaultListArg(210)
# print(dir(glass_4_2))
# print(glass_4_2.__dict__)
glass_4_3 = GlassDefaultListArg(210)


# print(dir(glass_4_3))
# print(glass_4_3.__dict__)


# 5. Создайте класс GlassAddRemove, добавьте методы add_water, remove_water
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
#    Вызовите методы add_water и remove.
#    Убедитесь, что методы правильно изменяют атрибут occupied_volume.


class GlassAddRemove:
    def __init__(self, capacity_volume, occupied_volume=0):
        if isinstance(capacity_volume, (int, float)):
            if capacity_volume > 0:
                self.capacity_volume = capacity_volume
            else:
                raise ValueError
        else:
            raise TypeError

        if occupied_volume > capacity_volume:
            raise ValueError('вы пытаетесь налить больше, чем влазиет')

        if isinstance(occupied_volume, (int, float)):
            if occupied_volume >= 0:
                self.occupied_volume = occupied_volume
            else:
                raise ValueError
        else:
            raise TypeError

    def add_water(self, adding_water):
        free_space = self.capacity_volume - self.occupied_volume  # объем пустого места в стакане
        if adding_water <= free_space:
            self.occupied_volume += adding_water
            return self.occupied_volume
        else:
            self.occupied_volume = self.capacity_volume
            return adding_water - free_space

    def remove_water(self, removing_water):
        if removing_water >= self.occupied_volume:
            raise ValueError('ошибка, пытаемся вылить больше, чем нолито')
        else:
            self.occupied_volume -= removing_water
            return self.occupied_volume


glass_5_1 = GlassAddRemove(200, 100)
glass_5_1.add_water(50)
print(glass_5_1.__dict__)
glass_5_1.remove_water(149)
print(glass_5_1.occupied_volume)

# 6. Создайте три объекта типа GlassAddRemove,
#    вызовите функцию dir для трёх объектов и для класса GlassAddRemove.
#    а. Получите типы объектов и класса
#    б. Проверьте тип созданного объекта.


glass_6_1 = GlassAddRemove(200, 50)
# print(dir(glass_6_1))
print(type(glass_6_1))
glass_6_2 = GlassAddRemove(200, 100)
# print(dir(glass_6_2))
glass_6_3 = GlassAddRemove(200, 150)
# print(dir(glass_6_3))
print(dir(GlassAddRemove))


# ---------------------------------------------------------------------------------------------
# Внутренние объекты класса (стр. 25-33)

# 7. Получите список атрибутов экземпляра класса в начале метода __init__, 
#    в середине __init__ и в конце __init__, (стр. 28-30)
#    а также после создания объекта.
#    Опишите результат.
class GlassAddRemoveBeep:
    def __init__(self, capacity_volume, occupied_volume=0):

        print(GlassAddRemoveBeep.__dict__)

        if isinstance(capacity_volume, (int, float)):
            if capacity_volume > 0:
                self.capacity_volume = capacity_volume
            else:
                raise ValueError
        else:
            raise TypeError

        if occupied_volume > capacity_volume:
            raise ValueError('вы пытаетесь налить больше, чем влазиет')

        print(GlassAddRemoveBeep.__dict__)

        if isinstance(occupied_volume, (int, float)):
            if occupied_volume >= 0:
                self.occupied_volume = occupied_volume
            else:
                raise ValueError
        else:
            raise TypeError

        print(GlassAddRemoveBeep.__dict__)


glass_7 = GlassAddRemoveBeep(200, 100)
print(glass_7.__dict__)


# 8. Создайте три объекта Glass. (стр. 27)
#    Получите id для каждого объекта с соответсвующим id переменной self.
class GlassId:
    def __init__(self, capacity_volume, occupied_volume=0):
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        # print(hex(id(self)))  # адрес в памяьи объекта self


glass_8_1 = GlassId(200)
print(hex(id(glass_8_1)))
glass_8_2 = GlassId(200)
print(hex(id(glass_8_2)))
glass_8_3 = GlassId(200)
print(hex(id(glass_8_3)))


# 9. Корректно ли следующее объявление класса с точки зрения:
#     - интерпретатора Python; -- КОРРЕКТНО
#     - соглашения о стиле кодирования -- НЕКОРРЕКТНО
#    Запустите код.


# ###########
# class d:
#     def __init__(f, a=2):
#         f.a = a
#
#     def print_me(p):
#         print(p.a)
#
# d.print_me(d())
#


# 10. Исправьте
class A:
    def __init__(self, a):
        if 10 < a < 50:
            # return  # он тут лишний, дальше код не выполнится и атрибут не создастся
            self.a = a;


obj_1 = A(25)
print(obj_1.__dict__)

obj_2 = A(100)
print(obj_2.__dict__)


# Объясните так реализовывать __init__ нельзя?
# НЕЛЬЗЯ РЕАЛИЗОВАТЬ


# 11. Циклическая зависимость (стр. 39-44)


class Node:
    def __init__(self, prev=None, next_=None):
        '''

        :param prev: # Class Node
        :param next_: #Class Node
        '''
        self.__prev = prev
        self.__next = next_

    def set_next(self, next_):
        self.__next = next_

    def set_prev(self, prev):
        self.__prev = prev

    def get_next(self, ):
        return self.__next

    def get_prev(self, ):
        return self.__prev

    def __str__(self):
        pass

    def __repr__(self):
        pass


class LinkedList:
    def __init__(self, nodes=None):
        if nodes is None:
            self.head = None
            self.tail = None
        elif isinstance(nodes, Node):
            self.head = nodes
            self.tail = nodes
        else:
            self.head = nodes[0]
            self.tail = nodes[-1]

    def insert(self, node, index=0):
        '''
        Insert Node to any place of LinkedList
        node - Node
        index - position of node
        '''
        # TODO index out of range
        current_node = self.head

        for i in range(index):
            current_node = current_node.get_next()

        current_node.set_prev(node)

        if index == 0:
            self.head = node

        pass

    def append(self, node):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        pass

    def clear(self):
        '''
        Clear LinkedList
        '''
        pass

    def find(self, node):
        pass

    def remove(self, node):
        pass

    def delete(self, index):
        pass

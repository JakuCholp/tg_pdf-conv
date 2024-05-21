# # '===========================Принципы ООП============================'
# # # 1. Наследование
# # # 2. Полиморфизм
# # # 3. Инкапсуляция
# # # 4. Абстракция
# # # 5. Ассоциация --> Композицию и Агрегацию

# # # Наследование - позволяет принимать раодительские методы и атрибуты
# # # Родительский класс - от которого происходит наследование методов и атрибутов
# # # Дочерний класс - класс который получает от родительского класса его методы и атрибуты

# # # class Animal: # Родительский класс
# # #     def say(self):
# # #         print('Я животное')
# # # class Dog(Animal): # Дочерний класс
# # #     def say(self):
# # #         super().say()
# # #         print('Если быть точным то собака!')
# # # class Cat(Animal): # Дочерний класс
# # #     def say(self):
# # #         print("Я кот!")

# # # cat1 = Cat()
# # # dog1 = Dog()
# # # cat1.say()
# # # dog1.say()

# # # class Person:
# # #     def __init__(self, name, age):
# # #         self.name = name
# # #         self.age = age

# # #     def info(self):
# # #         print(f'Меня зовут {self.name}, мне {self.age} лет')

# # # class Student(Person):
# # #     def __init__(self, name, age, univer):
# # #         super().__init__(name, age)
# # #         self.univer = univer
# # #     def info(self):
# # #         super().info()
# # #         print(f'Я учусь в университете {self.univer}')
# # # bob = Student('Bob', 20, 'Politex')

# # class Employee:
# #     bonus = 1.5
# #     def __init__(self, name, last_name, salary):
# #         self.name = name
# #         self.last_name = last_name
# #         self.salary = salary
# #     def get_full_name(self):
# #         return f'{self.name} {self.last_name}'
# #     def give_bonus(self):
# #         self.salary = self.salary * self.bonus
# #         return self.salary

# # class Developer(Employee):
# #     def __init__(self, name, last_name, salary, prog_lang):
# #         super().__init__(name, last_name, salary)
# #         self.prog_lang = prog_lang
# # class ProductManager(Employee):
# #     def __init__(self, name, last_name, salary, emps=None):
# #         super().__init__(name, last_name, salary)
# #         if emps == None:
# #             self.emps = []
# #         else:
# #             self.emps = emps
# #     def add_emp(self, emp):
# #         if emp not in self.emps:
# #             self.emps.append(emp)
# #         else:
# #             print('Этот разработчик уже находится  команде')
# #     def show_emp(self):
# #         result = []
# #         for emp in self.emps:
# #             result.append(emp.get_full_name())
# #         return result


# # dev1 = Developer('Bob', 'Snow', 1500, 'Python')
# # dev2 = Developer('John', 'Nix', 2000, 'Python + JS')
# # dev3 = Developer('Lary', 'London', 1200, 'Python')
# # dev4 = Developer('Karl', 'Liboski', 1400, 'JavaScript')
# # manager1 = ProductManager('Jasmina', 'Kanibekova', 1000, emps=[dev1,dev2])
# # manager2 = ProductManager('Alina', 'Kerimkulova', 800)

# # print(dev1.get_full_name())
# # print(dev1.give_bonus())
# # print(manager1.show_emp())
# # manager2.add_emp(dev4)
# # manager2.add_emp(dev2)
# # manager2.add_emp(dev3)
# # manager2.add_emp(dev3)
# # print(f'Менеджер: {manager2.get_full_name()}\nУправляет командой из разработчик:{", ".join(manager2.show_emp())}\nЕе зарплата составляет: {manager2.salary} ')

# class Device:
#     def __init__(self, serial_number):
#         self.serial_number = serial_number
#     def turn_on(self):
#         print('Устройсвто включилось')

# class Phone(Device):
#     def __init__(self, serial_number, brand, model, pixel):
#         super().__init__(serial_number)
#         self.brand = brand
#         self.model = model
#         self.pixel = pixel
#     def say_hello(self):
#         self.turn_on()
#         print(f'Привет я {self.brand}, {self.model} и моя камера имеет {self.pixel} пикселей')

# phone1 = Phone('AA2220', 'Apple', 'Iphone 15pro', 42)
# phone1.say_hello()

'''
Задание 2: Библиотека Книг
Создайте базовый класс Book с атрибутами title, author и pages. Затем создайте классы Ebook и PaperBook, которые наследуются от Book. Добавьте в классы методы для отображения информации о книге (display_info).'''

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
# class Ebook(Book):
#     # def __init__(self, title, author, pages):
#     #     super().__init__(title, author, pages)
#     def display_info(self):
#         print(f'nazvanie knigi {self.title}, avtor etoi knigi{self.author}, {self.pages} stranic, eto ebook')
# class PaperBook(Book):
#     # def __init__(self, title, author, pages):
#     #     super().__init__(title, author, pages)
#     def display_info(self):
#         print(f'nazvanie knigi {self.title}, avtor etoi knigi{self.author}, {self.pages} stranic, eto paperbook')

# kniga1 = Ebook('ak keme', 'Chyngyz Aitmatov', 350)
# kniga1.display_info()
# kniga1 = PaperBook('ak keme', 'Chyngyz Aitmatov', 350)
# kniga1.display_info()

'==============================Виды Наследования=========================='
'''
1. Одиночный
2. Множественный
3. Многоуровневый
4. Иерархический
5. Гибридный
'''
# Одиночное
class A:
    pass
class B(A):
    pass
# Множественное
class A:
    def info_(self):
        print('A')
class B:
    def info(self):
        print('B')
class C(A,B):
    # def info(self):
    #     print('C')
    pass
# obj_C = C()
# obj_C.info()
# print(C.mro()) # ирархия классов читается слева направо

# Многоуровневое
class A:
    a = 5
class B(A):
    pass
class C(B):
    pass
print(C.mro())
# object_c = C()
# print(object_c.a)

# Иерархический
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(A):
    pass

# Гибридный
class A:
    pass
class B:
    pass
class C(A,B):
    pass
class D(C):
    pass
class E(C):
    pass
class F(C):
    pass

# print(issubclass(F, D)) # проверка на наследование


# Создайте класс MyString, который будет наследоваться от str.

# Определите 2 своих метода:
# append, который будет принимать строку и добавлять её в конец исходной
# pop, который удаляет из строки последний элемент и возвращает его.
# Затем, создайте экземпляр example от класса MyString со значением String. Добавьте к example строку 'hello' методом append, затем примените метод pop.

class MyString(str):
    def __init__(self, stroka):
        self.stroka = stroka
    def append(self, new_string):
        self.stroka = self.stroka + new_string
        return self.stroka
    def pop(self):
        delete = self.stroka[-1]
        self.stroka = self.stroka[:-1]
        return delete

# string1 = MyString('hello')
# string1.append('world')
# print(string1.stroka)
# print(string1.pop())
# print(string1.stroka)


'''
Фигуры:

Создайте базовый класс Figure с методами для вычисления площади и периметра. Добавьте производные классы для следующих фигур:

Square (квадрат)
Rectangle (прямоугольник)
Circle (круг)
Каждый подкласс должен иметь соответствующие методы для расчета площади и периметра, а также метод draw(), который выводит текстовое или графическое представление фигуры.'''

'''
Зоопарк:

Создайте базовый класс Animal с атрибутами name, age, weight, и методом make_sound(), который выводит звук, издаваемый животным.

Создайте производные классы для следующих животных:

Dog (собака)
Cat (кошка)
Bird (птица)
Каждый подкласс должен иметь свой уникальный звук в методе make_sound(). Добавьте метод eat(), который имитирует процесс еды (например, вывод сообщения).'''

'''
Магазин электроники:

Создайте базовый класс Product с атрибутами name, price, brand, и методом get_description(), который возвращает строковое описание продукта.

Создайте производные классы:

Smartphone (смартфон) с атрибутами screen_size, os
Laptop (ноутбук) с атрибутами cpu, ram
TV (телевизор) с атрибутами screen_resolution, refresh_rate'''


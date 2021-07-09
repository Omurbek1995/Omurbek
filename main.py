 ### OOP
 ### Объектно-ориентированное программирование
 ###1) Encapsulation
 ###2) Polymorphism
 ###3) Inheritance
 ###4) Abstraction

# class Student:
#     pass
#
# student1 = Student()
# student2 = Student()
#
# # print(student1)
# # print(student2)
#
# student1.name = "Dima"
# student1.email = "dima@gmail.com"
# student1.age = "16"
#
# student2.name = "Emir"
# student2.email = "emir@gmail.com"
# student2.age = "13"
#
# # print(student1.name, student1.email, student1.age)
# # print(student2.name, student2.email, student2.age)
#
#
# class Employee:
#      def __init__(self, name, email, age):
#         self.name = name
#         self.email = email
#         self.age = age
#
#      def get_info(self):
#          return f'{self.name}, {self.email}", {self.age}'
#
#
#
#
# employee1 = Employee("Dima", "dima@gmail.com", 16)
# employee2 = Employee("Emir", "emir@gmail.com", 13)
#
#
# print(employee1)
# print(employee2)
#
# # print(employee1.name, employee1.email, employee1.age)
# # print(employee2.name, employee2.email, employee2.age)
#
# print(employee1.get_info())
# print(employee2.get_info())


class Employee:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def get_info(self):
        return f'{self.name}, {self.email}", {self.age}'

    def check_age(self):
        return "Not yet 18" if self.age < 18 else "legal to work"


# employee1 = Employee("Dima", "dima@gmail.com", 20)
# employee2 = Employee("Emir", "emir@gmail.com", 13)
#
# print(employee1)
# print(employee2)
#
# print(employee1.name, employee1.email, employee1.age)
# print(employee2.name, employee2.email, employee2.age)

# class Dog:
#     amount_of_legs = 4
#     def __init__(self, name, breed, color):
#         self.name = name
#         self.breed = breed
#         self.color = color
#         self.friends = []
#     def get_info(self):
#         return f"{self.name} {self.breed} {self.color}"
#
#     def bark(self):
#         return "Woof woof"
#
#     def eat(self, food):
#         return f"Woof {food} is a woof delicious"
#
#     def make_friend(self, friend):
#         self.friends.append(friend)
#         friend.friends.append(self)
#
#
# haski = Dog("Hatiko", "haski", "gray")
# retriever = Dog("Beathoven", "retriever", "golden")
# alabai = Dog("Max", "alabai", "black" )
# # print(haski.amount_of_legs)
# # print(retriever.amount_of_legs)
#
# print(haski.get_info())
# print(haski.bark())
# print(haski.eat("Bones"))
# haski.make_friend(retriever)
# # print(haski.friend.name)
# # print(retriever.friend.name)
# haski.make_friend(alabai)
# print(haski.friends)
#
# for friend in haski.friends:
#     print(friend.name, "retriever")


# class Cars:
#     type = "light"
#     area = "Bishkek"
#     state = "good"
#     def __init__(self, model, price, time, mileage, color, volume, remaining_petroleum):
#         self.model = model
#         self.price = price
#         self.time = time
#         self.mileage = mileage
#         self.color = color
#         self.volume = volume
#         self.remaining_petroleum = remaining_petroleum
#
#     def get_info(self):
#         return f"{self.model} {self.price} {self.time} {self.mileage} {self.color} {self.volume} {self.remaining_petroleum} " \
#                f"{self.type} {self.area} {self.state}"
#     def horning(self):
#         return "Beep Beep"
#
#
# Toyota = Cars("Toyota", "$5 000", 2010, 1000 , "white", 4.5, "150 lt")
# Honda = Cars("Honda", "$4 500", 2012, 850 , "black", 3.2, "50 lt")
# Hyundai = Cars("Hyundai", "$4 000", 2015, 800 , "red", 1.7, "25 lt")
#
# print(Toyota.get_info())
# print(Honda.get_info())
# print(Hyundai.get_info())
#
# print(Toyota.horning())
# print(Honda.horning())
# print(Hyundai.horning())

# 1) Создать класс дома
# 2) К дому добавить несколько атрибутов класса
# 3) Создать конструктор, со следующими аргументами
#  - Площадь
#  - Цена
#  - Адрес
#  - Год строительства
#  - Газ
#  - Электричество
#  - Канализация
#  - Мебель
# 4) Метод, который даст инфо о доме
# 5) Метод, который будет добавлять мебель в аттрибут мебель класса Дом
# 6) Каждая мебель будет занимать 40 кв м дома
# 7) Если общая площадь мебели равна или больше площади дома,
# то мы не сможем добавлять больше мебель


class House:
    def __init__(self, area, price, address, build_year, natural_gas, electricity, sewerage, furniture):
        self.area = area
        self.price = price
        self.address = address
        self.build_year = build_year
        self.natural_gas = natural_gas
        self.electricity = electricity
        self.sewerage = sewerage
        self.furniture = []

    def get_info(self):
        return f"The House1 area is {self.area} m2 {self.price} $ {self.address} {self.build_year} the natural gas {self.natural_gas} " \
               f" the electricity  {self.electricity} the sewerage {self.sewerage} amount of furnitures {self.furniture} pieces"


    def adding_furniture(self,furniture):
        self.furniture.append(furniture)
        furniture.adding_furniture.append(self)


House1 = House(100, 30000, "Chui str. 15/5", 2015, "exist", "exist", "exist", 2)
House2 = House(150, 45000, "Sovetskaya str. 21/10", 2016, "no", "exist", "exist", 3)
House3 = House(125, 35000, "Akhunbaeva str., 25", 2010, "exist", "exist", "exist", 2)


print(House1.get_info())
print(House2.get_info())
print(House3.get_info())



























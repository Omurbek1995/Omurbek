# class Animal:
#     amount_of_legs = 4
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#
#     def eat(self, food):
#         return f"I am eating {food}"
#
#
# a1 = Animal("animal1", "white")
# a2 = Animal("animal2", "black")
#
#
# class Dog(Animal):
#     follow_commands = True
#     def bark(self):
#         return "Woof"
#
# class Cat(Animal):
#     follow_command = False
#     def meow(self):
#         return "Meow"
#
# d1 = Dog("dog1", "black")
# print(d1.name, d1.amount_of_legs, d1.eat("bones"))
#
#
# c1 = Cat("cat1", "red")
# print(c1.name, c1.amount_of_legs, c1.eat("fish"))
#
# print(d1.follow_commands)
# print(c1.follow_command)
#
# print(d1.bark())
# print(c1.meow())


# print(a1.name, a1.color)
# print(a2.name, a1.color)

# class Human:
#     education = "Bachelor"
#     def __init__(self, name, age, experience):
#         self.name = name
#         self.age = age
#         self.experience = experience
#
#
# class Teacher(Human):
#     def work_place(self):
#         return "School"
# class Doctor(Human):
#     def work_place(self):
#         return "Hospital"
# class Banker(Human):
#     def work_place(self):
#         return "Bank"
#
# teacher = Teacher("Asan", 30, 7)
# doctor = Doctor("Aigul", 25, 2)
# banker = Banker("Beka", 35, 12)
# print(teacher.name, teacher.age, teacher.experience, teacher.education)
# print(doctor.name, doctor.age, doctor.experience, doctor.education)
# print(banker.name, banker.age, banker.experience, banker.education)
#
#
# print(teacher.work_place())
# print(doctor.work_place())
# print(banker.work_place())


class Form:

    def set_values(self, height, width):
        self.height = height
        self.width = width


class Square(Form):
    def area(self):
        return self.height * self.width

class Triangle(Form):
    def area(self):
        return (self.height * self.width)/2

square = Square()
triangle = Triangle()

square.set_values(5,4)
triangle.set_values(8,2)


# print(square.area())
# print(triangle.area())


class Human:
    def __init__(self, name, age, phone, address):
        self.name  = name
        self.age = age
        self.phone = phone
        self.address = address


    def sleep(self):
        return "I am sleeping"



class Developer(Human):
    def code(self):
        return "I am coding"

class Backenddeveloper(Developer):
    def create_apis(self):
        return "API creator"

class PythonDeveloper(Backenddeveloper):
    def develop_with_django(self):
        return "Django used for backend"
class PHPDeveloper(Backenddeveloper):
    def develop_with_laravel(self):
        return "Laravel used for backend"

class FrontendDeveloper(Developer):
    def code_html(self):
        return "HTML is done"

python_dev = PythonDeveloper("Pythonist", 25, "0555160795", "Bishkek")
php_dev = PHPDeveloper("PHPist", 23, "0703160795", "Karaganda")
js_developer = FrontendDeveloper("Frontend", 20, "0111111", "Tokmok")
# print(python_dev.develop_with_django())
# print(python_dev.create_apis())
# print(python_dev.code())
#
# print(php_dev.develop_with_laravel())
# print(php_dev.create_apis())
# print(php_dev.code())
#
# print(js_developer.code_html())
# print(js_developer.code())


# Создать класс User,
# Добавить к классу несколько аттрибутов и методов
#
# Создать класс RegisteredUser
# Наследуется от User
# Добавить к этому классу аттрубут registered = True
# Добавить к этому классу метод date_joined, который будет показывать дату,
# когда зарегистрировался пользователь
#
# Создать класс ActiveUser
# Наследуется от RegisteredUser
# Добавить к классу ActiveUser аттрибуты amount_of_posts_made
# и метод add_post,
# который при вызове увеличит значение аттрибута amount_of_posts_made на 1

# from datetime import datetime
#
# class User:
#     talking_ability = "yes"
#     moving_ability = "yes"
#     flying_ability = "no"
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.date_joined = datetime.now()
#
# class RegisteredUser(User):
#     registered = True
#     def get_date_joined(self):
#         return self.date_joined
#
#
# r1 = RegisteredUser("Omurbek", 25, "male")
# r2 = RegisteredUser("Ulan", 26, "male")
# print(r1.name, r1.age, r1.sex)
# print(r2.name, r2.age, r2.sex)
#
#
# print(r1.date_joined())
# print(r2.date_joined())
























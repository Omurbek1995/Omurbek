# class A:
#     x = 5
#
#
# class B:
#     x = 10
#
#
# class C(B, A):
#     pass


# c = C()
# print(c.x)


####mro = method resolution order = порядок разрешения методов


# class Donkey:
#     is_donkey = True
#
#
# class Horse:
#     is_horse = True
#
# class Mule(Donkey, Horse):
#     pass
#
# mule = Mule()
# # print(mule.is_horse)
# # print(mule.is_donkey)
#
# class Transport:
#     def drive(self):
#         print("arriving")
#
#
#     def carry_goods(self):
#         print("carrying goods")
#
#
# class Car(Transport):
#     def carry_passengers(self):
#         print("carrying passengers")
#
#
# class CraneMixing:
#     def lift(self):
#         print("lifting something")
#
#
# class TruckWithCrane(Transport, CraneMixing):
#     def carry_things(self):
#         print("carrying things")
#
#
# class MotorBoatWithCrane(Transport, CraneMixing):
#     def dock(self):
#         print("docked")

"""
# Создать класс PhoneMixin
# у класса есть метод call(), который будет звонить
#
# Создать класс Technology
# У класса будет метод charge(), который выдаст я заряжаюсь
#
# Создать класс MobilePhone и HomePhone,
# которые наслежуются от предыдущих классов
# у обоих классов есть свои аттрибуты и свои методы
#
# Создать класс Computer, который наследуется от класса Technology
# У экземпляра класа есть свои методы и аттрибуты
"""
class PhoneMixin:
    def call(self):
        print("calling")

class Technology:
    def charge(self):
        print("i am charging")


class MobilePhone(Technology, PhoneMixin):
    def mobile_phone(self, make_call, make_videocall, watch_video, listen_music):
        self.make_call = "make call"
        self.make_videocall = "video call"
        self.watch_video = "watch video"
        self.listen_music = "listen music"


class HomePhone(Technology, PhoneMixin):
    def home_phone(self, make_calling):
        self.make_calling = "make calling"





















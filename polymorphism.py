class Cow:
    can_milk = True


class Horse:
    can_milk = False


class Mule(Cow, Horse):
    can_milk = False


m = Mule()
# print(m.can_milk)



class Form:
    def __init__(self, a, b):
        self.a = b
        self.b = b


    def area(self):
        return f"{self.a}, {self.b}"

class Square(Form):
    def area(self):
        return (self.a) * (self.b)


class Rectangle(Form):
    def area(self):
        return (self.a + self.b) * 2


class Circle(Form):
    pass


square = Square(4,3)
rectangle = Rectangle(2,3)
circle = Circle(8,7)


# print(square.area())
# print(rectangle.area())
# print(circle.area())


class Pizza:
    def __init__(self, size, ingredients):
        self.size = size
        self.ingredients = ingredients


class Margharita(Pizza):
    def __init__(self):
        super().__init__(23, ["tomato", "oreghano"])


class FourCheese(Pizza):
    def __init__(self):
        super().__init__(23, ["mozarello", "cheese2", "cheddar"])


pizza = Pizza(25, ["mushrooms", "chicken"])
margharita = Margharita()
four_cheese = FourCheese()

# print(pizza.ingredients)
# print(margharita.ingredients)
# print(four_cheese.ingredients)



class Universities:
    def __init__(self, students, teachers):
        self.students = students
        self.teachers = teachers


class Alatoo(Universities):
    def __init__(self):
        super().__init__(1500, 50)


class Manas(Universities):
    def __init__(self):
        super().__init__(2000, 80)

#
# alatoo = Alatoo























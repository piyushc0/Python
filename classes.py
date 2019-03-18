class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("moved")

    def draw(self):
        print("drawing")


point = Point(10, 20)
point.x = 11
print(point.x)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


piyush = Person("Piyush Choubey")
piyush.talk()


# Inheritance
class Mammals:
    def walk(self):
        print("Walking")


class Dog(Mammals):
    def bark(self):
        print("bark")


class Cat(Mammals):
    def meow(self):
        print("meow")


dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.meow()


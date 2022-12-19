"""Dog class"""


class Dog:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def walking(self):
        print(f"{self.name}, is walking.")

    def barking(self, phrase):
        print(f"{self.name}, says {phrase}")

    def eating(self, food):
        print(f"{self.name} is eating {food}")

    def sitting(self):
        print(f"{self.name} is sitting")


rex = Dog("Rex")
rex.barking("Huff-Huff")
rex.walking()
rex.eating("sausage")
rex.sitting()

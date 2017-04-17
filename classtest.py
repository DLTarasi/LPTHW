class Human(object):
    def __init__(self, name, age):
        self.name = name

        self.age = age

class Male(Human):
    def __init__(self, name, age, height):
        Human.__init__(self, name, age)
        self.height = height

dave = Male("Dave", 31, 72)

print(f"{dave.name} is a human that is {dave.age} years old and {dave.height} inches tall.")

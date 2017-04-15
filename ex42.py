## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

#Dog is-a animal (is a object)
class Dog(Animal):

    def __init__(self, name):
        # dog has-a name
        self.name = name

# Cat is a Animal (is a object)
class Cat(Animal):

    def __init__(self, name):
        # cat has a name
        self.name = name

# person is a object
class Person(object):

    def __init__(self, name):
        #person has a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

# Employee is-a person (is a object)
class Employee(Person):

    def __init__(self, name, salary):
        #Employee has a name?
        super(Employee, self).__init__(name)
        #emplyee has a salary
        self.salary = salary

# fish is-a object
class Fish(object):
    pass

# salmon is-a Fish (is a object)
class Salmon(Fish):
    pass

# halibut is-a fish (is a object)
class Halibut(Fish):
    pass


## rover is-a Dog (named Rover)
rover = Dog("Rover")

# satan is a cat(Named satan)
satan = Cat("Satan")

# Mary is-a person
mary = Person("Mary")

# mary has-a pet that is a named satan
mary.pet = satan

# frank is a employee (which is a person which is an object) with name Frank and has a salary of 120,000
frank = Employee("Frank", 120000)

# frank has a pet named rover
frank.pet = rover

#flipper is a fish (is an object)
flipper = Fish()

# crouse is a salmon (is a fish is a object)
crouse = Salmon()

# harry is a halibut (is a fish is a object)
harry = Halibut()

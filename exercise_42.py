'''useful docstring'''

##Animal is-a object
class Animal(object):
    pass

##dog is a Animal
class Dog(Animal):
    def __init__(self, name):
        ##name of dog
        self.name = name
##cat is a Animal
class Cat(Animal):
    def __init(self, name):
        ##name of cat
        self.name = name
##Person is a object        
class Person(object):
    def __init__(self, name):
        ##name of person
        self.name = name
        #person has a pet of some kind
        self.pet = None
##employee is a person        
class Employee(Person):
    def __init__(self, name, salary):
    ##super returns an object from the parent class  per W3Schools
    super(Employee, self).__init__(name)
    ##employee has a salary
    self.salary = salary

##fish is a object
class Fish(object):
    pass

##Salmon is a fish
class Salmon(Fish):
    pass

##Halibut is a fish
class Halibut(Fish):
    pass

##rover is a dog
rover = Dog("Rover")

#satan is a cat
satan = Cat("Satan")

#Mary is a person
mary = Person("Mary")

##Mary has a pet, satan
mary.pet = satan

##frank is an employee his salary is 120000
frank = Employee("Frank, 120000")
##frank has a pet named rover
frank.pet = rover

##flipper is a fish
flipper = Fish()

#crouse is a salmon
crouse = Salmon()

##harry is a halibut
harry = Halibut()
## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## ��Dog
class Dog(Animal):

    def __init__(self, name):
        ## ��ʼ��name
        self.name = name

## ��Cat
class Cat(Animal):

    def __init__(self, name):
        ## ��ʼ��Cat��name
        self.name = name

## ��Person
class Person(object):

    def __init__(self, name):
        ## ��ʼ��Person��name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## ��Employee
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ��ʼ��salary
        self.salary = salary

## ��Fish
class Fish(object):
    pass

## ��Salmon
class Salmon(Fish):
    pass

## ��Halibut
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## ʵ��������satan
satan = Cat("Satan")

## ʵ��������mary
mary = Person("Mary")

## ��petʵ�������Ը�ֵ
mary.pet = satan

## ʵ��������ֵ
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()
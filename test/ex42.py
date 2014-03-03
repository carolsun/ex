## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## 类Dog
class Dog(Animal):

    def __init__(self, name):
        ## 初始化name
        self.name = name

## 类Cat
class Cat(Animal):

    def __init__(self, name):
        ## 初始化Cat的name
        self.name = name

## 类Person
class Person(object):

    def __init__(self, name):
        ## 初始化Person的name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## 类Employee
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## 初始化salary
        self.salary = salary

## 类Fish
class Fish(object):
    pass

## 类Salmon
class Salmon(Fish):
    pass

## 类Halibut
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## 实例化对象satan
satan = Cat("Satan")

## 实例化对象mary
mary = Person("Mary")

## 将pet实例化属性赋值
mary.pet = satan

## 实例化并赋值
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()
'''Q1'''
'''In object-oriented programming (OOP), a class is a blueprint or a template for creating objects. It defines the properties
(attributes) and behaviors (methods) that objects of that class will have. In other words, a class provides a way to define and encapsulate
data and functionality together.
An object, on the other hand, is an instance of a class. It is created using the blueprint defined by the class. An object has its own unique
identity, state, and behavior. You can think of an object as a specific realization of a class, with its own set of values for the attributes
 defined in the class.Here's an example in Python to illustrate the concept of class and object:'''
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = 0

    def accelerate(self, increment):
        self.speed += increment

    def brake(self, decrement):
        self.speed -= decrement


# Creating objects of the Car class
car1 = Car("Toyota", "Camry", "Red")
car2 = Car("Honda", "Accord", "Blue")

# Accessing object attributes
print(car1.brand)  # Output: Toyota
print(car2.model)  # Output: Accord

# Calling object methods
car1.accelerate(20)
car2.brake(10)

print(car1.speed)  # Output: 20
print(car2.speed)  # Output: -10

'''Q2'''
'''The four pillars of Object-Oriented Programming (OOP) are:

1. Encapsulation: Encapsulation is the principle of bundling data (attributes) and methods (functions) together within a class. 
It allows for the hiding of internal implementation details and provides access to the object's behavior through well-defined interfaces. 
Encapsulation promotes data integrity, code modularity, and information hiding.
2. Inheritance: Inheritance is a mechanism that allows a class (derived class or subclass) to inherit properties and behaviors from another 
class (base class or superclass). The derived class can extend or modify the functionality inherited from the base class, promoting code 
reuse and providing a hierarchical structure for organizing classes.
3. Polymorphism: Polymorphism means the ability of objects of different classes to respond to the same message or method in different ways. 
It allows objects of different types to be treated as objects of a common superclass. Polymorphism is achieved through method overriding and 
method overloading. Method overriding involves redefining a method in a subclass to provide a different implementation than the one in the 
superclass. Method overloading allows multiple methods with the same name but different parameters to exist in the same class.
4. Abstraction: Abstraction is the process of simplifying complex systems by breaking them down into smaller, more manageable parts. 
It focuses on capturing the essential features and behavior of an object while hiding unnecessary details. Abstraction is achieved 
through abstract classes and interfaces. An abstract class is a class that cannot be instantiated and serves as a blueprint for derived 
classes. It can contain abstract methods, which are methods without an implementation. Interfaces define a contract for a set of methods 
that a class must implement, providing a way for objects to be used interchangeably based on their shared behavior.
These four pillars form the foundation of OOP and provide principles and concepts to design and structure software systems in a modular, 
flexible, and maintainable manner.'''

'''Q3'''
'''In object-oriented programming (OOP), the __init__() function, also known as the constructor, is a special method that is automatically 
called when an object is created from a class. It is used to initialize the attributes of the object and perform any necessary setup or 
initialization tasks.
The primary purpose of the __init__() function is to set the initial state of the object by assigning values to its attributes. 
It allows you to define the initial values of the object's attributes based on the arguments passed during object creation.
Here's an example to illustrate the use of the __init__() function in Python:'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Creating an object of the Person class
person = Person("Alice", 25)

# Accessing the object's attributes
print(person.name)  # Output: Alice
print(person.age)   # Output: 25

# Calling the object's method
person.greet()  # Output: Hello, my name is Alice and I am 25 years old.

'''Q4'''
'''In object-oriented programming (OOP), self is a convention used to refer to the instance of a class within its own methods. 
It is a reference to the object itself and allows access to the attributes and methods of that object.
The use of self is important because it distinguishes between instance variables and local variables within a class. 
When a method is called on an object, the self parameter is automatically passed as the first argument. This allows the method to access 
and modify the object's attributes and invoke other methods defined within the class.
Here's an example to illustrate the use of self in Python:'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Creating an object of the Person class
person = Person("Alice", 25)

# Calling the greet() method
person.greet()

'''Q5'''
'''Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called a subclass or derived class) 
to inherit properties and behaviors from another class (called a superclass or base class). The subclass can extend or modify the 
functionality inherited from the superclass, promoting code reuse and providing a hierarchical structure for organizing classes.
There are different types of inheritance relationships:
Single Inheritance: In single inheritance, a subclass inherits from a single superclass. This is the simplest form of inheritance.
Example:'''
class Animal:
    def eat(self):
        print("Eating...")


class Dog(Animal):
    def bark(self):
        print("Barking...")


# Creating an object of the Dog class
dog = Dog()

# Accessing methods from both Animal and Dog classes
dog.eat()   # Output: Eating...
dog.bark()  # Output: Barking...
'''Multiple Inheritance: Multiple inheritance allows a subclass to inherit from multiple superclasses. 
The subclass can inherit and combine the attributes and methods of all the superclasses.
Example:'''
class A:
    def method_a(self):
        print("Method A")


class B:
    def method_b(self):
        print("Method B")


class C(A, B):
    def method_c(self):
        print("Method C")


# Creating an object of the C class
c = C()

# Accessing methods from A, B, and C classes
c.method_a()  # Output: Method A
c.method_b()  # Output: Method B
c.method_c()  # Output: Method C
'''Multilevel Inheritance: Multilevel inheritance involves a chain of inheritance, where a subclass inherits from another subclass, 
creating a hierarchical structure.
Example:'''
class Vehicle:
    def drive(self):
        print("Driving...")


class Car(Vehicle):
    def park(self):
        print("Parking...")


class SportsCar(Car):
    def race(self):
        print("Racing...")


# Creating an object of the SportsCar class
sports_car = SportsCar()

# Accessing methods from all three classes
sports_car.drive()  # Output: Driving...
sports_car.park()   # Output: Parking...
sports_car.race()   # Output: Racing...

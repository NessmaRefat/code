'''
  Basics in python.
'''


'''
  Hello World.
'''
print("Hello, World!")

############
'''
  Variables.
'''
x = 5
y = "John"
print(x)
print(y)

############

'''
  Data Types.
'''
x = 5
y = 3.14
z = "Hello"
w = None
print(type(x))
#‹class 'int'>
print(type(y))
# => ‹class "flot'>
print(type(z))
# => ‹class 'str'›
print(type(w))
#‹class "NoneType">

##############
'''
  Operators.
'''
x = 5
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)

###################

'''
  Conditional Statements.
'''
x = 5
if x > 3:
    print("x is greater than 3")
else:
    print("x is not greater than 3")

###############

'''
  Loops.
'''
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

i = 0
while i < 5:
    print(i)
    i += 1

################
'''
  Getting user input.
'''
name = input("What is your name? ")
print("Hello, " + name + "!")

##############

'''
  String manipulation.
'''
text = "Hello, World!"
print(text.upper())
print(text.lower())
print(text.replace("Hello", "Hi"))

###############
'''
   Lists.
'''
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(len(fruits))
fruits.append("orange")
print(fruits)

###############

'''
  Dictionaries.
'''
person = {"name": "John", "age": 30, "city": "New York"}
print(person)
print(person["name"])
person["age"] = 40
print(person)

##############

'''
  Functions.
'''
def greet(name):
    print("Hello, " + name + "!")

greet("John")
###########
def rectangle_area(width, height):
    return width * height


area = rectangle_area(5, 10)
print(area)

length = 4.2
height = 3.5
area = length * height
prim = 2 * (length + height)  print	area, prim
############
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(is_even(4))
print(is_even(5))
########################
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
fibonacci(10)
#####################
def sort_numbers(numbers):
    numbers.sort()
    return numbers


numbers = [3, 1, 4, 2, 5]
sorted_numbers = sort_numbers(numbers)
print(sorted_numbers)
###########################
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


temperature_f = 68
temperature_c = fahrenheit_to_celsius(temperature_f)
print(temperature_c)
#########################

'''
  loops.
'''
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
###################
num = 1

while num <= 10:
    print(num)
    num += 1
#####################
word = "Python"

for char in word:
    print(char)
##################
num = 1
total = 0

while num <= 10:
    total += num
    num += 1

print(total)
#######################
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end='\t')
    print()
#########################

'''
  Exceptions.
'''
try:
    x = int("hello")
except ValueError:
    print("Could not convert input to integer")

################
'''
  modules.
'''
import requests

response = requests.get('https://www.google.com')
print(response.status_code) # prints the status code of the response
print(response.text) # prints the content of the response
###################
import numpy as np

arr = np.array([1, 2, 3])
print(arr) # prints the array [1, 2, 3]
print(np.mean(arr)) # prints the mean of the array
#####################
import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df) # prints the data frame
print(df['age'].mean()) # prints the mean age
#########################
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [4, 5, 6]
plt.plot(x, y)
plt.show() # displays the plot
######################
'''
  break and continue.
'''
# Using break to exit a loop early
for i in range(10):
    if i == 5:
        break
    print(i)

# Output: 0 1 2 3 4

# Using continue to skip over certain iterations
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Output: 1 3 5 7 9
##########################

'''
  pass.
'''
# Using pass as a placeholder
for i in range(10):
    if i == 5:
        pass
    else:
        print(i)

# Output: 0 1 2 3 4 6 7 8 9
###################
if traffic_light == "green" :
    pass # to implement later
else:
    stop()
##################

'''
  scope.
'''
def my_function():
    # Local variable
    x = 10
    print("Inside the function:", x)

# Call the function
my_function()

# Try to access the variable outside the function (will result in an error)
# Uncommenting the line below will raise a NameError
# print("Outside the function:", x)

'''
  Functions within functions.
'''
def function1(x):
    def function2(y):
        print y + 2
        return y + 2
    return 3 * function2(x)

# call the function
a = function1(2) # what is the output
print (a)
b = function2(2.5) # what is the result of that
#####################
'''
  Global Keyword.
'''
x = 0
def incr_x():
    x = x + 1 # does not work
def incr_x2():
    global x
    x = x	+ 1 # does work

##############
'''
  Default arguments
'''
def greet(name, greeting="Hello"):
    """
    Function to greet a person with a default greeting.

    Parameters:
    - name (str): The name of the person to greet.
    - greeting (str): The greeting message (default is "Hello").
    """
    print(f"{greeting}, {name}!")

# Example usage without providing the 'greeting' argument
greet("Alice")  # Output: Hello, Alice!

# Example usage with a custom greeting
greet("Bob", "Hi")  # Output: Hi, Bob!

##################
'''
  Doc-string.
'''
def greet(name, greeting="Hello"):
    """
    Function to greet a person with a default greeting.

    Parameters:
    - name (str): The name of the person to greet.
    - greeting (str): The greeting message (default is "Hello").

    Returns:
    None
    """
    print(f"{greeting}, {name}!")
###################
'''
  Functions modify lists
'''
def modify_items(L):
    L[0] = 0
A = [1,	2,	3]
print (A)	#	[1,	2,	3]
modify_items(A)
print (A)	# [0,	2, 3]
################

''''
  List comprehension
'''
# Example 1: Create a list of squares for numbers 0 to 9
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Example 2: Create a list of even numbers from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# Example 3: Convert a list of temperatures from Celsius to Fahrenheit
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = [((9/5) * temp + 32) for temp in celsius_temps]
print(fahrenheit_temps)  # Output: [32.0, 50.0, 68.0, 86.0, 104.0]
########################

'''
  Tuples.
'''
myTuple = (1, 2, 3)
print myTuple[1]
# 2
print myTuple[1:3]
# (2, 3)
###################

'''
  Packaging and unpacking.
'''
t = 1, 2, 3
x, y,	z = t
print(t)	#	(1,	2,	3)
print(y)	#	2
################

'''
  Creating Sets.
'''
# Creating an empty set
empty_set = set()
print(empty_set)  # Output: set()

# Creating a set with elements
fruits = {'apple', 'banana', 'orange'}
print(fruits)  # Output: {'orange', 'banana', 'apple'}

# Creating a set from a list
numbers = set([1, 2, 3, 4, 4, 5])  # Note: Duplicates are automatically removed
print(numbers)  # Output: {1, 2, 3, 4, 5}
################
'''
  Set Operations
'''
# Adding elements to a set
fruits.add('grape')
print(fruits)  # Output: {'orange', 'banana', 'grape', 'apple'}

# Removing elements from a set
fruits.remove('banana')
print(fruits)  # Output: {'orange', 'grape', 'apple'}

# Checking membership
print('apple' in fruits)  # Output: True

# Set union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # or use set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Set intersection
intersection_set = set1 & set2  # or use set1.intersection(set2)
print(intersection_set)  # Output: {3}

# Set difference
difference_set = set1 - set2  # or use set1.difference(set2)
print(difference_set)  # Output: {1, 2}

# Set symmetric difference
symmetric_difference_set = set1 ^ set2  # or use set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
#################################################################################

'''
  oop.
'''

'''
  Attributes and methods.
'''
import numpy as np
a = np.array([1,2,3,4])   # shape attribute
a.shape
#############
import numpy as np
a = np.array([1,2,3,4])   # reshape method
a.reshape(2,2)
############

'''
  Add methods to a class
'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        if not self.is_running:
            print(f"The {self.year} {self.make} {self.model} is starting.")
            self.is_running = True
        else:
            print("The car is already running.")

    def stop(self):
        if self.is_running:
            print(f"The {self.year} {self.make} {self.model} is stopping.")
            self.is_running = False
        else:
            print("The car is already stopped.")

    def honk(self):
        print("Beep! Beep!")

# Creating an instance of the Car class
my_car = Car(make="Toyota", model="Camry", year=2022)

# Using the methods
my_car.start()  # Output: The 2022 Toyota Camry is starting.
my_car.honk()   # Output: Beep! Beep!
my_car.stop()   # Output: The 2022 Toyota Camry is stopping.
#################################

'''
  Add an attribute to class
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_adult = age >= 18  # New attribute

# Creating an instance of the Person class
person1 = Person(name="Alice", age=25)

# Accessing the attributes
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")
print(f"Is Adult: {person1.is_adult}")
#################
'''
  inheritance.
'''
class Base(object):

	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name


# Inherited or Sub class (Note Person in bracket)
class Child(Base):

	# Constructor
	def __init__(self, name, age):
		Base.__init__(self, name)
		self.age = age

	# To get name
	def getAge(self):
		return self.age

# Inherited or Sub class (Note Person in bracket)


class GrandChild(Child):

	# Constructor
	def __init__(self, name, age, address):
		Child.__init__(self, name, age)
		self.address = address

	# To get address
	def getAddress(self):
		return self.address


# Driver code
g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())
#################
'''
  program to illustrate private access modifier in a class.
'''
class Geek:
    # private members
    __name = None
    __roll = None
    __branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    # private member function
    def __displayDetails(self):
        # accessing private data members
        print("Name: ", self.__name)
        print("Roll: ", self.__roll)
        print("Branch: ", self.__branch)

    # public member function
    def accessPrivateFunction(self):
        # accessing private member function
        self.__displayDetails()

    # getter method for name
    def get_name(self):
        self.__name

    # setter method name
    def set_name(self, name):
        self.__name = name

    # getter method for roll
    def get_roll(self):
        self.__roll

    # setter method roll
    def set_roll(self, roll):
        self.__roll = roll

    # getter method for branch
    def get_branch(self):
        self.__branch

    # setter method branch
    def set_branch(self, branch):
        self.__branch = branch

    # creating object
obj = Geek("Osama", 1706256, "Information Technology")

# calling public member function of the class
obj.accessPrivateFunction()
####################################

class A(object):
    def __init__(self, x):
        self.x = x

    def getX(self):
        return self.X

    # Based on condition C inherits


# from A or it inherits from
# object i.e. does not inherit A
cond = True


# inherits from A or B
class C(A if cond else object):
    def isA(self):
        return True


# Object of C_A
ca = C(1)
print(ca.isA())
#######################
"""
Class or Static Variables

> a static variable is a variable that is shared among all instances of a class, 
    rather than being unique to each instance.

> Static variables are defined inside the class definition, but outside of any method definitions. 

> They are typically initialized with a value, just like an instance variable, 
  but they can be accessed and modified through the class itself, rather than through an instance.    
"""
class CSStudent:
	stream = 'cse'				 # Class Variable (Static)
	def __init__(self,name,roll):
		self.name = name		 # Instance Variable
		self.roll = roll		 # Instance Variable

# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

print(a.stream) # prints "cse"
print(b.stream) # prints "cse"
print(a.name) # prints "Geek"
print(b.name) # prints "Nerd"
print(a.roll) # prints "1"
print(b.roll) # prints "2"

# Class variables can be accessed using class
# name also
print(CSStudent.stream) # prints "cse"
# To change the stream for all instances of the class we can change it
# directly from the class
CSStudent.stream = 'mech'

print(a.stream) # prints 'mech'
print(b.stream) # prints 'mech'
###########################

"""
    Method Overriding in Python
"""
class Parent():

    # Constructor
    def __init__(self):
        self.value = "Inside Parent"

    # Parent's show method
    def show(self):
        print(self.value)

    # Defining child class


class Child(Parent):

    # Constructor
    def __init__(self):
        self.value = "Inside Child"

    # Child's show method
    def show(self):
        print(self.value)

    # Driver's code


obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()

print('################################################')


# Python program to demonstrate
# calling the parent's class method
# inside the overridden method


class Parent():

    def show(self):
        print("Inside Parent")


class Child(Parent):

    def show(self):
        # Calling the parent's class
        # method
        Parent.show(self)  # or super().show()
        print("Inside Child")

    # Driver's code


obj = Child()
obj.show()

#############################
"""
    Method Overloading in Python

    Two or more methods have the same name but different numbers of parameters or different types 
    of parameters, or both. These methods are called overloaded methods and this is called method 
    overloading. 

    Like other languages (for example, method overloading in C++) do, python does not support method 
    overloading by default. But there are different ways to achieve method overloading in Python. 
"""


# First product method.
# Takes two argument and print their
# product


def product(a, b):
    p = a * b
    print(p)


# Second product method
# Takes three argument and print their
# product


def product(a, b, c):
    p = a * b * c
    print(p)


# Uncommenting the below line shows an error
# product(4, 5)


# This line will call the second product method
product(4, 5, 5)

print('####################################################')


# Function to take multiple arguments
def add(datatype, *args):
    # if datatype is int
    # initialize answer as 0
    if datatype == 'int':
        answer = 0

    # if datatype is str
    # initialize answer as ''
    if datatype == 'str':
        answer = ''

    # Traverse through the arguments
    for x in args:
        # This will do addition if the
        # arguments are int. Or concatenation
        # if the arguments are str
        answer = answer + x

    print(answer)


# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'Geeks')

print('####################################################')

# code
def add(a=None, b=None):
    # Checks if both parameters are available
    # if statement will be executed if only one parameter is available
    if a != None and b == None:
        print(a)
    # else will be executed if both are available and returns addition of two
    else:
        print(a + b)


# two arguments are passed, returns addition of two
add(2, 3)
# only one argument is passed, returns a
add(2)

print('####################################################')

'''
  Method Overriding in Python.
'''


from multipledispatch import dispatch


# passing one parameter


@dispatch(int, int)
def product(first, second):
    result = first * second
    print(result)


# passing two parameters


@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)


# you can also pass data type of any value as per requirement


@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)


# calling product method with 2 arguments
product(2, 3)  # this will give output of 6

# calling product method with 3 arguments but all int
product(2, 3, 2)  # this will give output of 12

# calling product method with 3 arguments but all float
product(2.2, 3.4, 2.3)  # this will give output of 17.985999999999997
#########################################

'''
  solid.
'''

'''
  Single Responsibility Principle (SRP).
A class should have only one reason to change, meaning it should only have one responsibility.
'''
class Report:
    def __init__(self, content):
        self.content = content

    def generate_report(self):
        # Generate report logic here
        print(f"Generating report: {self.content}")

class ReportPrinter:
    def print_report(self, report):
        # Print report logic here
        print(f"Printing report: {report.content}")

# Each class has a single responsibility
report = Report("Sales data")
printer = ReportPrinter()

report.generate_report()
printer.print_report(report)
################

'''
Open/Closed Principle (OCP):
A class should be open for extension but closed for modification.
'''
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# New shapes can be added without modifying existing code
shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(f"Area: {shape.area()}")
###############

'''
  Liskov Substitution Principle (LSP):
Subtypes must be substitutable for their base types without altering the correctness of the program.
'''

class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

class Penguin(Bird):
    def swim(self):
        print("Penguin swimming")

# Code should work with any subtype of Bird
def make_bird_fly(bird):
    bird.fly()

sparrow = Sparrow()
penguin = Penguin()

make_bird_fly(sparrow)
# make_bird_fly(penguin)  # Uncommenting this line would result in an error since Penguin does not have a fly method
####################

'''
Interface Segregation Principle (ISP):
A class should not be forced to implement interfaces it does not use.
'''

class Worker:
    def work(self):
        pass

class Eater:
    def eat(self):
        pass

class Robot(Worker):
    def work(self):
        print("Robot working")

# Robot does not need to implement the eat method
robot = Robot()
robot.work()
# robot.eat()  # Uncommenting this line would result in an error since Robot does not have an eat method
##################

'''
Dependency Inversion Principle (DIP):
High-level modules should not depend on low-level modules. Both should depend on abstractions.
'''

class LightBulb:
    def turn_on(self):
        print("Light bulb turned on")

class Switch:
    def __init__(self, device):
        self.device = device

    def operate(self):
        self.device.turn_on()

# Switch does not depend on a specific type of device, only on abstractions
bulb = LightBulb()
switch = Switch(bulb)
switch.operate()

###############################################################




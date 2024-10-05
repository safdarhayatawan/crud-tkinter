Lecture : Creating a class & class attributes


class Product:
 
    quantity = 200
 
 
product1 = Product()
 
print(product1)
 
print(product1.quantity)
 
product2 = Product()
print(product2.quantity)


Lecture : Instance attributes & constructor


class Product:
    quantity = 200
 
    
    def __init__(self,name,price):
        
        self.name = name
        
        self.price = price
 
 
product2 = Product("Phone",500)
print(product2.name)
print(product2.price)
 


Lecture : Methods


class Product:
    quantity = 200
 
    def __init__(self,name,price):
        self.name = name
        self.price = price
 
    def summer_discount(self,discount_percent):
        self.price = self.price - (self.price *discount_percent/100)
 
product1 = Product("Laptop",500)
print(product1.price)
 
#let's call the method on object here
product1.summer_discount(10)
print(product1.price)
.

Lecture : Function based v/s OOP based way of writing code


def product_data():
    product_name = input('Enter name of product')
    product_price = input('Enter price of product')
    print(product_name)
    print(product_price)
 
product_data()


class Product:
 
    def __init__(self,name,price):
        self.name = name
        self.price = price
 
    def get_data(self):
        self.name = input('Enter name')
        self.price = input('Enter price')
 
    def put_data(self):
        print(self.name)
        print(self.price)
 
product1 = Product("","")
product1.get_data()
product1.put_data()


Lecture : Inheritance


class Product:
 
    def __init__(self,name,price):
        self.name = name
        self.price = price
 
    def get_data(self):
        self.name = input('Enter name')
        self.price = input('Enter price')
 
    def put_data(self):
        print(self.name)
        print(self.price)
 
class DigitalProduct(Product):
 
    def __init__(self,link):
        self.link = link
 
    def get_link(self):
        self.link = input('Enter product link')
 
    def put_link(self):
        print(self.link)
 
ebook = DigitalProduct("")
ebook.get_data()
ebook.get_link()
ebook.put_data()
ebook.put_link()


Lecture : Multiple inheritance


class A:
    def method_a(self):
        print('Method of class A')
 
class B:
    def method_b(self):
        print('Method of class B')
 
class C(A,B):
    def method_c(self):
        print('Method of class C')
 
cobject = C()
cobject.method_a()
cobject.method_b()
cobject.method_c()


Lecture 8: Multi-level inheritance


class A:
    def method_a(self):
        print('Method of class A')
 
class B(A):
    def method_b(self):
        print('Method of class B')
 
class C(B):
    def method_c(self):
        print('Method of class C')
 
cobject = C()
cobject.method_a()
cobject.method_b()
cobject.method_c()


Lecture : Polymorphism


print(10+20)
print('Hello'+'world')


# In this case python counts the number of characters in a string
print(len('HelloWorld'))
# In this case python counts the number of items in a list
print(len(['Apple','Mango','Banana']))


Lecture : Method overriding


class Food:
    def type(self):
        print("Food")
 
class Fruit(Food):
    def type(self):
        print('Fruit')
 
burger = Food()
print(burger.type())
# this invokes the method in the Food class
 
apple = Fruit()
print(apple.type())
# The method in the Fruit class overrides the method in the Food class.
.

Lecture : Operator overloading


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
 
    #To overload the + operator, we use the __add__ method
    # To perform overloading, python provides a special method
    # to overload the + operator we use the magic method __add__
 
    # we want the plus operator to perform addition of two Points/ two objects
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        #once we have the values of x and y we want to return then into a point
        return Point(x,y)
 
point1 = Point(1,2)
point2 = Point(3,4)
print(point1+point2)


def __str__(self):
        return '({0},{1})'.format(self.x,self.y)


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
 
   
 
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        #once we have the values of x and y we want to return then into a point
        return Point(x,y)
 
    def __str__(self):
        return '({0},{1})'.format(self.x,self.y)
 
point1 = Point(1,2)
point2 = Point(3,4)
print(point1+point2)


Lecture: Instance Methods
class Student:
 
    def __init__(self, name):
        self.name = name
 
    def hello(self):
        print(f"Hello, my name is {self.name}")
 
    def name_length(self):
        return len(self.name)
 
# create an instance of the class
student1 = Student("John")
student1.hello()
length = student1.name_length()
print(length)


Lecture: Class Methods
class Student:
    # class variable
    category = 'student'
 
    def __init__(self, name):
        self.name = name
 
    def hello(self):
        print(f"Hello, my name is {self.name}")
 
    def name_length(self):
        return len(self.name)
 
    @classmethod
    def info(cls):
        print(f"This is a method of the class {cls.category}")
 
Student.info()


Lecture: Static Methods
class Student:
    # class variable
    category = 'student'
 
    def __init__(self, name):
        self.name = name
 
    def hello(self):
        print(f"Hello, my name is {self.name}")
 
    def name_length(self):
        return len(self.name)
 
    @classmethod
    def info(cls):
        print(f"This is a method of the class {cls.category}")
 
    @staticmethod
    def add(a, b):
        print(a+b)
 
Student.add(2, 4)


Another example:

class Circle:
    @staticmethod
    def area(r):
        return 3.14*r*r
 
    @staticmethod
    def circumfurence(r):
        return 2*3.14*r
 
# calling static methods
a = Circle.area(10)
print(a)
c = Circle.circumfurence(10)
print(c)




Lecture: Nested Classes In Python
class Car:
    def __init__(self, brand):
        self.brand = brand
        # create an object of the inner class
        self.steering_obj = self.Steering()
 
    def drive(self):
        print('Drive')
 
    class Steering:
        # this inner class will now have acess to the outer class
        def rotate(self):
            print("Rotate")
 
# now let's create an object of the outer class
# create instance of the outer class
car = Car("ABC")
# access the attribute of the outer class
print(car.brand)
# access method of outer class
car.drive()
 
# access  the inner class using the outer object
steering = car.steering_obj
# now access the inner method
steering.rotate()
Another example:

class Zoo:
    def __init__(self):
        # iniitially no animals in the zoo
        # create a list called animals
        self.animals = []
 
    # create a method that adds animal to above list
    def add_animal(self, name, species):
        # now to add an animal, create an object from below class
        animal = self.Animal(name, species)
        # now append this animal to the animals list
        self.animals.append(animal)
 
    class Animal:
        def __init__(self, name, species):
            self.name = name
            self.species = species
 
        def display_info(self):
            print(f"Name:{self.name}, Species:{self.species}")
 
# first create a zoo
my_zoo = Zoo()
 
# Add animals to the zoo
my_zoo.add_animal("Lion", "Mammal")
my_zoo.add_animal("Eagle", "Bird")
my_zoo.add_animal("Crocodile", "Reptile")
 
# Display information about the animals
for animal in my_zoo.animals:
    animal.display_info()


Lecture: Constructor Inheritance
class Parent:
    def __init__(self):
        self.balance = 50000
 
    def display_balance(self):
        print(f"Parent's property is {self.balance}")
 
class Child(Parent):
    pass
 
mike = Child()
mike.display_balance()


Lecture: Overriding Superclass Constructor
class Parent:
    def __init__(self):
        self.balance = 50000
 
    def display_balance(self):
        print(f"Parent's property is {self.balance}")
 
class Child(Parent):
    def __init__(self):
        self.balance = 20000
 
    def display_balance(self):
        print(f"Child's balance is {self.balance}")
 
mike = Child()
mike.display_balance()


Lecture: Super
class Parent:
    def __init__(self):
        self.parent_balance = 50000
 
    def display_balance(self):
        print(f"Parent's property is {self.parent_balance}")
 
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_balance = 20000
 
    def display_balance(self):
        print(f"Child's balance is {self.child_balance + self.parent_balance}")
 
mike = Child()
mike.display_balance()


Lecture: Entire OOP Example
# super class
class Vehicle:
    # defining a class attribute
    class_attribute = "This is a vehicle"
 
    # creating a constructor with parameters
    def __init__(self, name, color):
        self.name = name
        self.color = color
 
    # instance method
    def display_info(self):
        print(f"Name:{self.name}, Color:{self.color}")
 
    # class method
    @classmethod
    # passing class to the method
    def class_method(cls):
        print('This is a class method')
        # accessing a class attribute
        print(f"I can access class attribute {cls.class_attribute}")
 
    # static method
    @staticmethod
    def static_method():
        # does not access class or instance attribute
        print("I am a static method, I cannot access anything")
 
# subclass inheriting from Vehicle super class
 
class Car(Vehicle):
    # subclass consctuctor
    def __init__(self, name, color, fuel_type):
        # using super function to invoke init method of the superclass
        # so that we can access name and color attributes
        super().__init__(name, color)
        # creating own instance attribute of a subclass
        self.fuel_type = fuel_type
 
    # sub class overriding the display info method from the superclass
    def display_info(self):
        print(f"{self.name},{self.color},{self.fuel_type}")
 
# creating object of the superclass
vehicle = Vehicle("CoolCar", "Red")
# invoking instance method
vehicle.display_info()
# creating object of subclass
car = Car("LuxuryCar", "Black", "Petrol")
# inviking overriden method
car.display_info()
# acccessing class attribute directly from the class
print(Vehicle.class_attribute)
 
# inoking static method.
Vehicle.static_method()


Lecture: Student Management System Using OOP
class Student:
    def __init__(self,name,roll_number,age):
        self.name=name
        self.roll_number=roll_number
        self.age=age
        
class School:
    def __init__(self):
        self.students = []
    
    def add_student(self,name,roll_number,age):
        #create a student object
        student=Student(name,roll_number,age)
        self.students.append(student)
        print(f"Student {name} added successfully")
        
    def display_students(self):
        if self.students:
            for student in self.students:
                print(f"Name:{student.name}")
                print(f"Roll number:{student.roll_number}")
                print(f"Age:{student.age}")
                print("...................")
                
    def edit_student(self,roll_number,new_name,new_age):
        for student in self.students:
            if student.roll_number == roll_number:
                student.name=new_name
                student.age= new_age
                print(f"Student {student.name} successfully updated")
                return
    
    def delete_student(self,roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print(f"Student {student.name} deleted successfully.")
                return
        
#Create a school object first:
school = School()
while True:
    choice = input('Enter your choice: \\n1)Add student \\n2)Display list of students \\n3)Edit student data \\n5)Exit: ')
    if choice=="1":
        name = input('Enter name')
        roll_number= input('Enter roll number')
        age = input('Enter age')
        school.add_student(name, roll_number, age)
        
    elif choice =="2":
        school.display_students()
    elif choice =="3":
        roll_number = input("Enter roll number of student you want to edit")
        new_name = input("Enter new name for the student")
        new_age = input("Enter new age for the student")
        school.edit_student(roll_number, new_name, new_age)
    elif choice=="4":
        roll_number= input("Enter roll number you want to delete")
        school.delete_student(roll_number)
    elif choice=="5":
        break
Section Notes
Classes in Python:

Classes are a collection of objects.

They not only help us categorise objects, but also allow us to create objects. Classes are like blueprints for creating objects.

For example, if we want to save products, we can create a class called Product:

class Product:
    # Now we need some attributes to define the class. 
    # These are called class attributes.
    # Class attributes remain the same for every object.
    quantity = 200
 
# We can create an object out of the class, like this:
# Creating a product1 object from the Product class:
product1 = Product()
# Now product1 is an object. Let's print it:
print(product1)
# When we run this, we get the product object. Instead of printing the object itself, we can print one of its attributes:
# Let's print quantity:
print(product1.quantity)
# Here we have created a class, created a class attribute, and printed it. The class attribute gets assigned to all objects that we create from that class.
# Let's create another product:
product2 = Product()
print(product2.quantity)
# It has the same quantity. But what about properties like price, product name, etc.? We want different names and prices for different products.
# In that case, we need to use instance attributes, not class attributes.


Instance attributes & constructor:

Instance attributes cannot be created directly inside a class because the value of that attribute gets assigned to all objects which are created from that class.

To define instance attributes, we need to use a constructor.

So, what is a constructor?

A constructor is a method that is automatically executed when we create an object of that class. It is like a function definition.

Here's an example of how to create a constructor:

class Product:
    quantity = 200
 
    # We will learn about self later. Self means a reference to that particular
    # object itself.
    # __ in Python means that the function is created for internal use
    # and should not be called directly by users.
    # It is a convention used to indicate that the function is private.
    # Pass instance attributes here.
    # We pass name as a parameter because when we create an object, we have to
    # pass in the name argument.
    def __init__(self, name, price):
        # Let's create instance attributes here.
        # The following line sets this object's name to the name argument
        # that is passed.
        self.name = name
        # We can add multiple instance attributes to a class.
        # Let's also add price as well.
        self.price = price
 
# Now let's try creating an object out of it.
#product1 = Product()
#print(product1)
# This will give an error because we have not passed the arguments for the
# name and price parameters.
# which means when we create an object, we need to also pass in the name
# and the price of that object.
 
# Let's do that now.
product2 = Product("Phone", 500)
print(product2.name)
print(product2.price)


Methods:

Now that we have a product, let's say we want to apply a summer discount to the prices.

To implement this, we need to write code. If we were using a function-based approach, we would have created a function and written the logic inside it to calculate and return a discount.

But in OOP, we create methods instead of functions. Methods are similar to functions, but they are declared inside a class because they belong to that class.

These methods are also called instance methods because they can modify the attributes of the object.

For example, as the discount method only has to work with products, it makes sense to add it inside the Product class. Let's create that discount method here:

class Product:
    quantity = 200
 
    def __init__(self, name, price):
        self.name = name
        self.price = price
 
    def summer_discount(self, discount_percent):
        self.price = self.price - (self.price * discount_percent/100)
 
# create an object of Product
product1 = Product("Laptop", 500)
print(product1.price)
 
# call the method on the object here
product1.summer_discount(10)
print(product1.price)
This code creates a Product object and sets its initial price to 500. We then call the summer_discount() method on the product1 object, passing in a 10% discount. The method calculates the new price based on the discount and updates the price attribute of the object. Finally, we print the new price to confirm that the discount has been applied.



Polymorphism:

Polymorphism simply means the ability to take multiple forms. A real-world example of polymorphism would be a person.

When a person is at school, they are a student.

When a person is at work, they are an employee, and at home, they are a family member.

This means that a person's role changes depending on the context.



Python is polymorphic, meaning that a single operator, function, or class method in Python can have multiple uses.

For example, the + operator can be used to add two numbers as well as concatenate two strings:

print(10+20)
print('Hello'+'world')
This is called operator polymorphism in Python.



Similarly, we also have function polymorphism.

Some functions in Python are polymorphic, meaning their behavior changes depending on the data we pass to them.

For example, the len function can count the number of characters in a string or the number of items in a list:

print(len('HelloWorld'))
print(len(['Apple','Mango','Banana']))
Similar to this, we have polymorphism in OOP as well.



Method overriding:

In general terms, overriding means to use your authority to reject somebody’s decision or order, to be more important than something.

For example, a manager can fire an employee, but a CEO can reject this decision.

Method overriding is a type of polymorphism in Python.

To understand this, let’s take an example, we can define a Food class with a method called type(). Then, we can define another class called Fruit that inherits from the Food class and also has a method called type().

If we create an object of the Fruit class and call the type() method, it will override the type() method of the Food class.

Here's the example code:

class Food:
    def type(self):
        print("Food")
 
class Fruit(Food):
    def type(self):
        print('Fruit')
 
burger = Food()
print(burger.type())
# this invokes the method in the Food class
 
apple = Fruit()
print(apple.type())
# The method in the Fruit class overrides the method in the Food class.


Operator overloading:

Operator overloading allows you to overload operators like + and - and change their behaviour.

For example, we can use + to perform addition of two numbers.

Let’s say we want to overload the + operator:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    # To overload the + operator, we use the __add__ method
    # To perform overloading, Python provides a special method
    # To overload the + operator, we use the magic method __add__
 
    # We want the plus operator to perform addition of two Points/two objects
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        # Once we have the values of x and y we want to return them into a point
        return Point(x, y)
 
    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)
 
point1 = Point(1, 2)
point2 = Point(3, 4)
print(point1 + point2)
Now the above code returns an object, so we need to define the format in which the result should be returned.



To do this, we use a str method, which returns a human-readable or string representation of an object.

Hence, we add this to the class:

def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)


Here's the entire code:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    # To overload the + operator, we use the __add__ method
    # To perform overloading, Python provides a special method
    # To overload the + operator, we use the magic method __add__
 
    # We want the plus operator to perform addition of two Points/two objects
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        # Once we have the values of x and y we want to return them into a point
        return Point(x, y)
 
    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)
 
point1 = Point(1, 2)
point2 = Point(3, 4)
print(point1 + point2)











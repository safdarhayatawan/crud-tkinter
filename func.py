# Source code
# Lecture: Functions in Python

def hello():
    print('Hello')
    print('Hi')
    print('Tom')
	


hello()
hello()


# Lecture: Passing arguments to function

def add():
    a= 10
    b= 20
    print(a+b)
 
add()
def add(a,b):
    print(a+b)
 
add()
add(10,20)
add(20,40)
add(34,23)


Lecture: Keyword arguments

def speed(distance,time):
    s = distance/time
    return s
 
avgspeed = speed(100,2)
print(avgspeed)
 
avgspeed = speed(2,100)
print(avgspeed)
 


Calling the above function with keyword arguments

avgspeed = speed(time=2,distance=100)
print(avgspeed)


Lecture: Default parameters

def area(pi,radius):
    a = pi * radius * radius
    return a
 
circle_area = area(3.14,10)
print(circle_area)


Making the pi argument as default argument

def area(radius,pi=3.14):
 


Now even if you don’t pass in the value of PI in the function call it still works fine

circle_area = area(10)


Passing pi as 3.15

circle_area = area(10,3.15)


Lecture: Making function return a value

def add(a,b):
    c= a+b
    return c
 
result = add(10,20)
print(result)


Lecture: calling a function inside another function

def add(a,b):
    return a+b
 
def square(c):
    return c*c
 
result = square(add(2,3))
print(result)


Lecture: Returning multiple values from a function

def circle(r):
    area = 3.14*r*r
    circumfurence = 2*3.14*r
    return area,circumfurence
 
# calling the function and extracting the value
a,c = circle(10)
print(f"Area of a circle is {a}, circumference is {c}")


Lecture: Passing list to a function

def sum(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total
 
result = sum([1,2,3,4,5])
print(result)


Lecture: Returning a list

def remove_duplicates(numbers):
    # create a new list which does not contain duplicates
    new_list =[]
    for number in numbers:
        if number not in new_list:
            new_list.append(number)
    return new_list
 
list = [1,2,3,4,3,4,5,2,1,7,8,9]
result = remove_duplicates(list)
print(result)
A simpler way is by using set()

Take the list, pass it to the set it will remove the duplicate elements.

Then convert the set back into a list:

def remove_duplicates(lst):
    return list(set(lst))


Lecture: Global & Local Variables

def add():
    count =1
    print(count)    
    
def sub():
    count =2
    
    print(count)
    
sub()
add()


Lecture: Accessing global variable inside a function

count = 10
 
def increment():
    global count
    count = count + 1
    print(count)
    
    
increment()


Lecture: Check if a string is palindrome

word = "panasonic"
# treat a string like a list
print(word[0])
 
# get the length of string
l = len(word)
 
# loop through all the items from the start
print('Printing the string straight')
for i in range(l):
    print(word[i])
    
# loop through the items in reverse
print('Printing the string in reverse')
for i in range(l):
    print(word[l-i-1])
    
#comparing and returning if palindrome
palindrome_flag = True
for i in range(l):
    if word[i] != word[l-i-1]:
        palindrome_flag = False
        break
    else:
        palindrome_flag = True
 
if palindrome_flag:
    print("The string is a palindrome")
else:
    print('The string is not a palindrome')
    
 
#converting the above code into a function
def check_palindrome(word):
    #get the length of the string
    l = len(word)
    for i in range(l):
        if word[i] != word[l-i-1]:
            return False
    return True
    
# call the above function
print(check_palindrome("racecar"))


Lecture: EMI Calculator

#formula to calculate emi is: P x R x (1+R)^N / [(1+R)^N-1]
#P: Principal loan amount = INR 10,000,00
 
#N: Loan tenure in months = 120 months
 
#R: Interest rate per month [7.2/12/100] = 0.006
 
def emi_calculator(principal,rate,time):
    #calculate the monthly rate
    r = rate/12/100
    emi = (principal * r * (1+r)**time) / ((1+r)**time -1 )
    return emi
 
#checking the function
print(emi_calculator(4858900, 8.75, 240))


Lecture: Factorial Using Recursion in Python

Python code to calculate factorial:

def factorial(number):
    if number ==1:
        return 1
    else:
        return number * factorial(number-1)
    
print(factorial(4))
 
#how the iterations work
#factorial(4) => return 4 * factorial(3)
#factorial(3) => return 3 * factorial(2)
#factorial(2) => return 2 * factorial(1)
#factorial(1) => return 1
Lecture: Variable length positional arguments

def add(*args):
    sum = 0
    for n in args:
        sum = sum+n
    print(sum)
 
add()
add(10)
add(20, 30)
add(40, 50, 60)


Lecture: Variable length keyword arguments

def product(**kwargs):
    for key, value in kwargs.items():
        print(key+":"+value)
 
product(name='iphone', price="700")
product(name='iPad', price="400", description="This is an ipad")


Lecture: Decorators in Python

def chocolate():
    print('chocolate')
chocolate()


def chocolate():
    print('chocolate')
 
# this decorator function accepts function as argument
 
def decorator(func):
    # inside the decorator function we have another function
    def wrapper():
        print('Wrapper up side')
        # now here I call the func
        func()
        print('Wrapper down side')
    # now the decorator needs to return this wrapper
    return wrapper
 
# now to call the functions, i first call the decorator and then pass chocolate inside it
# then assign the function back to the previous main function i.e chocolate
# finally call the chocolate function
chocolate = decorator(chocolate)
chocolate()


def decorator(func):
    # inside the decorator function we have another function
    def wrapper():
        print('Wrapper up side')
        # now here I call the func
        func()
        print('Wrapper down side')
    # now the decorator needs to return this wrapper
    return wrapper
 
@decorator
def chocolate():
    print('chocolate')
 
chocolate()
Lecture: Reusing decorators

@decorator
def cake():
    print('cake')
 
cake()


Lecture: Decorating functions which accept arguments

@decorator
def cake(name):
    print('cake'+name)
 
cake("apple")


def decorator(func):
    def wrapper(name):
        print('Wrapper up side')
        func(name)
        print('Wrapper down side')
    return wrapper


chocolate()


def decorator(func):
    def wrapper(*args, **kwargs):
        print('Wrapper up side')
        func(*args, **kwargs)
        print('Wrapper down side')
    return wrapper
 
@decorator
def chocolate():
    print('chocolate')
 
@decorator
def cake(name):
    print('cake'+name)
 
chocolate()
cake("Mango")


Lecture: Decorating functions that return a value

def total(price):
    # Let's assume there was some code here which calculated the total amount
    return price
Now let’s create a decorator for it:

def summer_discount_decorator(func):
    def wrapper(price):
        # take the value inside the total and return
        func(price)
        return func(price/2)
    return wrapper
Entire code:

def summer_discount_decorator(func):
    def wrapper(price):
        # take the value inside the total and return
        func(price)
        return func(price/2)
    return wrapper
 
@summer_discount_decorator
def total(price):
    # Let's assume there was some code here which calculated the total amount
    return price
 
print(total(20))












Course content
Play
94. Functions
9min
Play
95. Passing Arguments To Functions
8min
Play
96. Keyword Arguments
4min
Play
97. Default Parameters
5min
Play
98. Making function return a value
8min
Play
99. Calling a function in other function
2min
Play
100. Making A Function Return Multiple Values
5min
Play
101. Passing List To A Function
6min
Play
102. Returning List
7min
Play
103. Local & Global Variables
5min
Play
104. Accessing Global Variables Inside A Function
4min
Play
105. Check If A String Is A Palindrome
11min
Notes
Functions in Python:

A function in Python is a block of code that performs a specific task.

It can be created to avoid repeating code and to make the program more efficient.

To create a function in Python, we need to define it first. The syntax for defining a function is as follows:

def function_name():
    # code to be executed


The def keyword is used to define the function, followed by the name of the function and a pair of parentheses.

Any arguments that the function takes can be specified within these parentheses.

The colon : is used to indicate the start of the function block.

The code to be executed inside the function must be indented. It is best practice to use four spaces for indentation.

For example, let's define a function called hello:

def hello():
    print('Hello')
    print('Hi')
    print('Tom')


To execute the function, we simply call it by its name followed by a pair of parentheses. For example, we can call the hello function twice:

hello()
hello()


When we run the code, it will print the output of the hello function twice, which is:

Hello
Hi
Tom
Hello
Hi
Tom


Passing arguments to function:

let's say we want to create a function that adds two numbers:

def add():
    a = 10
    b = 20
    print(a + b)
 
add()
This works, but the problem is that every time we call the add() function, it performs the addition of 10 and 20.

However, we want our function to be dynamic, i.e., it should perform the addition of any two numbers we want, just like the print() function.



To make a function accept arguments, we have to change its definition. Let's modify the function definition for add() so that instead of having variables a and b inside the function, we make them parameters:

def add(a, b):
    print(a + b)
 
add()
Now calling the add() function gives an error because the function call now expects two arguments.



Let's pass values to the function call and see the result:

def add(a, b):
    print(a + b)
 
add(10, 20)
Note: In the above code, a and b are parameters, and 10 and 20 are arguments.


In the above code, what happens is that the value 10 gets assigned to a, and 20 gets assigned to b.

You can even verify that by printing them:

pythonCopy code
def add(a, b):
    print(a)
    print(b)
    print(a + b)
 
add(10, 20)
This is why they are called positional arguments.



Let's call this function multiple times with different values:

add(10, 20)
add(20, 40)
add(34, 23)


Positional arguments:

In positional arguments, the position of arguments matters, and you must know the position of the parameters so that you could pass them accurately.

But let’s say you don't want to be bothered by the position of the argument.

Let’s take an example to understand this. Let’s create a function that calculates the speed.

def speed(distance,time):
    s = distance/time
    return s


As we are using positional arguments, we always have to remember that while calling a function, we need to pass the arguments in the proper order.

If we pass arguments in the wrong order, the function returns a wrong result. For instance:

avgspeed = speed(100,2)
print(avgspeed)
 
avgspeed = speed(2,100)
print(avgspeed)


However, we can call the same function using keyword arguments, which do not require the order of arguments to be the same as the parameter order in the function definition. For example:

avgspeed = speed(time=2,distance=100)
print(avgspeed)
Now in the above code, even if we pass arguments in the wrong order, we do not have to worry about the result being wrong.



Default parameters:

While defining a function, we can add parameters to it. However, we can also pass the values to these parameters inside the function definition itself, which is called passing default parameters.



Let’s take an example:

def area(pi, radius):
    a = pi * radius * radius
    return a
 
circle_area = area(3.14, 10)
print(circle_area)


Now let's make the pi argument a default argument:

def area(radius, pi=3.14):


Even if we don’t pass the value of PI in the function call, it still works fine:

circle_area = area(10)


You can also override the value of the default parameter by passing your own value. Let’s pass pi as 3.15:

circle_area = area(10, 3.15)
Now the value of 3.14, which is the default parameter, gets overridden by the value which we pass in the function call.



Making a function return a value:

The "add" function above prints a value, but suppose we want to access that value instead of printing it. In this case, we need to modify the function definition to return the value using the "return" keyword:

def add(a, b):
    c = a + b
    return c
 
result = add(10, 20)
print(result)
This is a common practice in real-world function design, where functions often return a value that can be used in other parts of the program.



Returning multiple values from a function.

Till this point we have learned how to return a single value from a function.

However, we can also make a function return multiple values as well.

Here is how:

# returning multiple values from a function
 
def circle(r):
    area = 3.14*r*r
    circumfurence = 2*3.14*r
    return area,circumfurence
 
# calling the function and extracting ghe value
a,c = circle(10)
print(f"Area of a circle is {a}, circumference is {c}")


Passing different data structures to a function:

We cannot just pass a single integer or a string to a function, we can also pass some complex data structure like a list to a function.

Here is an example of passing an entire list to a given function.

def sum(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total
 
result = sum([1,2,3,4,5])
print(result)
Remove duplicates from a list:

Using a combination of a loop, "in" and append, we can remove duplicate values from a list.

def remove_duplicates(numbers):
    # create a new list which does not contain duplicates
    new_list =[]
    for number in numbers:
        if number not in new_list:
            new_list.append(number)
    return new_list
 
list = [1,2,3,4,3,4,5,2,1,7,8,9]
result = remove_duplicates(list)
print(result)
A simpler way is by using set()

Take the list, pass it to the set it will remove the duplicate elements.

Then convert the set back into a list:

def remove_duplicates(lst):
    return list(set(lst))
Local & global variables.



Global variables:



Global variables are defined outside of any function or block and can be accessed throughout the program.

They have global scope, meaning they can be accessed by any part of the program, including functions and blocks.

Global variables are typically defined at the top level of the program.

To define a global variable, you simply assign a value to a variable outside of any function or block.

Global variables can be accessed and modified by any part of the program unless they are shadowed by a local variable with the same name inside a function.



Local variables:



Local variables are defined within a function or block and can only be accessed within that specific function or block.

They have local scope, meaning they are limited in visibility to the block in which they are defined.

Local variables are typically defined inside functions, loops, or conditional statements.

To define a local variable, you assign a value to a variable inside a function or block.

Local variables can only be accessed and modified within the function or block in which they are defined. They are not visible outside of their scope.

Let's take an example to understand global and local variables.



count = 10 #this is called a global variable
print(count)
 
def add():
		# when we declare a variable inside a function it becomes a local variable
		# scope of a global variable is limited to the function, we cannot access 
		# its value outside the fuction
 
    count = 20
    print(count)
    
add()
Let’s take another example

def add():
    count = 20
    print(count)
    
print(count)
This wont work because the variable count is local variable and it cannot be accessed outside the variable.

A variable created in one function cannot be accessed in other function either.

Let’s create two functions with variable count.

def add():
    count =1
    print(count)    
    
def sub():
    count =2
    
    print(count)
    
sub()
add()
Accessing global variable inside a function

count = 10
 
def increment():
    print(count)
    
    
increment()
This will work because count here is a global variable.

A global variable is accessible everywhere outside as well as inside the function as well.

But now let’s try incrementing the value of count inside the function.

count = 10
 
def increment():
    count = count + 1
    print(count)
    
    
increment()
This gives an error and the error log says, local variable cannot be referenced before assignment.

This does not work because Python thinks that the variable declared inside the function is a local variable.

To access global variable inside a function, we need to tell python that “count” is a global variable.

We do this using the global keyword.

count = 10
 
def increment():
    global count
    count = count + 1
    print(count)
    
    
increment()


Check if a given string is palindrome:

A palindrome is a string which when reversed gives the exact same output.

The code below explain step by step how a string could be checked for being a palindrome.

To check the first letters and last letters of a string, we first loop through the string in a forward manner and then also loop though it in reverse and compare the letters if they match.

To loop in a reverse manner, we simply use the length of the string and subtract 1 from it every time the loop executes.

If the string is found not to be a palindrome, we set the palindrome_flag to false.

word = "panasonic"
# treat a string like a list
print(word[0])
 
# get the length of string
l = len(word)
 
# loop through all the items from the start
print('Printing the string straight')
for i in range(l):
    print(word[i])
    
# loop through the items in reverse
print('Printing the string in reverse')
for i in range(l):
    print(word[l-i-1])
    
#comparing and returning if palindrome
palindrome_flag = True
for i in range(l):
    if word[i] != word[l-i-1]:
        palindrome_flag = False
        break
    else:
        palindrome_flag = True
 
if palindrome_flag:
    print("The string is a palindrome")
else:
    print('The string is not a palindrome')
    
 
#converting the above code into a function
def check_palindrome(word):
    #get the length of the string
    l = len(word)
    for i in range(l):
        if word[i] != word[l-i-1]:
            return False
    return True
    
# call the above function
print(check_palindrome("racecar"))
EMI calculator:

#formula to calculate emi is: P x R x (1+R)^N / [(1+R)^N-1]
#P: Principal loan amount = INR 10,000,00
 
#N: Loan tenure in months = 120 months
 
#R: Interest rate per month [7.2/12/100] = 0.006
 
def emi_calculator(principal,rate,time):
    #calculate the monthly rate
    r = rate/12/100
    emi = (principal * r * (1+r)**time) / ((1+r)**time -1 )
    return emi
 
#checking the function
print(emi_calculator(4858900, 8.75, 240))
Recursion:

Recursion in python, in simple term means a function calling itself.

def hello():
    print('Hello')
    hello()
    
    
hello()
How factorial is calculated mathematically:

4! = 4x3x2x1
2! = 2x1
100! = 100x99x98......
Python code to calculate factorial:

def factorial(number):
    if number ==1:
        return 1
    else:
        return number * factorial(number-1)
    
print(factorial(4))
 
#how the iterations work
#factorial(4) => return 4 * factorial(3)
#factorial(3) => return 3 * factorial(2)
#factorial(2) => return 2 * factorial(1)
#factorial(1) => return 1
Variable length positional arguments:

In some cases we don’t know the number of arguments we need to pass to a function.

Example:

A function sum which can accepts any number of numbers to be added.

Hence to create a function that can accept variable number of arguments we use variable length arguments.

Variable length arguments are defined by *args.

When we pass arguments to *args it stores it in a tuple.

A program that can add any numbers passed to it.

def add(*args):
    sum = 0
    for n in args:
        sum = sum+n
    print(sum)
 
add()
add(10)
add(20, 30)
add(40, 50, 60)
Variable length keyword arguments:

A variable length keyword arguments let’s you pass any number or arguments along with a keyword rather than the position.

def product(**kwargs):
    for key, value in kwargs.items():
        print(key+":"+value)
 
product(name='iphone', price="700")
product(name='iPad', price="400", description="This is an ipad")
Decorators in Python:

In simple words, decorators are a function that take another function and extends its behaviour without altering the code.

Let’s take an example to understand this.

def chocolate():
    print('chocolate')
chocolate()
When we call this, it simply prints chocolate.

Now let’s say I want to add a wrapper to the chocolate which prints wrapper and wrapper before and after chocolate.

To do this, we use a decorator function.

def chocolate():
    print('chocolate')
 
# this decorator function accepts function as argument
 
def decorator(func):
    # inside the decorator function we have another function
    def wrapper():
        print('Wrapper up side')
        # now here I call the func
        func()
        print('Wrapper down side')
    # now the decorator needs to return this wrapper
    return wrapper
 
# now to call the functions, i first call the decorator and then pass chocolate inside it
# then assign the function back to the previous main function i.e chocolate
# finally call the chocolate function
chocolate = decorator(chocolate)
chocolate()
As you can see now the behaviour of the chocolate function is modified.

Hence we can say that decorators simply wrap the function to modify its behaviour.

Another way of using decorator:

In the above code after defining two functions we had to write the last 2 lines to use the decorator.

However, instead of that we can also use a simpler way.

def decorator(func):
    # inside the decorator function we have another function
    def wrapper():
        print('Wrapper up side')
        # now here I call the func
        func()
        print('Wrapper down side')
    # now the decorator needs to return this wrapper
    return wrapper
 
@decorator
def chocolate():
    print('chocolate')
 
chocolate()
Reusing decorators:

Decorators can be reused as well.

The decorator we used for wrapping can also be used for another function as well.

let’s create another function called cake.

@decorator
def cake():
    print('cake')
 
cake()
Decorating functions which accept an argument:

Let’s try adding some argument to the cake function and see if it works.

@decorator
def cake(name):
    print('cake'+name)
 
cake("apple")
This will give us an error, because the wrapper which calls the function does not accept any arguments.

Hence we need to make the func() inside the wrapper accept arguments as well.

def decorator(func):
    def wrapper(name):
        print('Wrapper up side')
        func(name)
        print('Wrapper down side')
    return wrapper
Now this works.

However when we now try to use the same decorator with chocolate it wont work because we have not passed in name there.

Try doing it:

chocolate()
To avoid this, we pass variable length arguments and variable length keyword arguments to the function instead of simply passing it name.

def decorator(func):
    def wrapper(*args, **kwargs):
        print('Wrapper up side')
        func(*args, **kwargs)
        print('Wrapper down side')
    return wrapper
 
@decorator
def chocolate():
    print('chocolate')
 
@decorator
def cake(name):
    print('cake'+name)
 
chocolate()
cake("Mango")
Now both of them work well.



Decorating functions that return a value:

Let’s assume we have a function that calculates the total amount of shopping.

On top of it, we want another function that calculates a 50% summer discount on the total value.

Create a function called total that calculates the total price:

def total(price):
    # Let's assume there was some code here which calculated the total amount
    return price
Now let’s create a decorator for it:

def summer_discount_decorator(func):
    def wrapper(price):
        # take the value inside the total and return
        func(price)
        return func(price/2)
    return wrapper
Entire code:

def summer_discount_decorator(func):
    def wrapper(price):
        # take the value inside the total and return
        func(price)
        return func(price/2)
    return wrapper
 
@summer_discount_decorator
def total(price):
    # Let's assume there was some code here which calculated the total amount
    return price
 
print(total(20))
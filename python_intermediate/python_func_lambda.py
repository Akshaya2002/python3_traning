# Python lambda Syntax ---> lambda arguments : expression

string ='GeeksforGeeks'
  
# lambda returns a function object 
print(lambda string : string)

x ="GeeksforGeeks"
  
# lambda gets pass to print  
(lambda x : print(x))(x)

# Python program to illustrate cube of a number   
# showing difference between def() and lambda().  
  
def cube(y):  
    return y*y*y;  
    
g = lambda x: x*x*x  
print(g(7))  
    
print(cube(5))

def power(n): 
    return lambda a : a ** n 
  
# base = lambda a : a**2 get  
# returned to base 
base = power(2) 
  
print("Now power is set to 2") 
  
# when calling base it gets  
# executed with already set with 2 
print("8 powerof 2 = ", base(8)) 
  
# base = lambda a : a**5 get  
# returned to base 
base = power(5) 
print("Now power is set to 5") 
  
# when calling base it gets executed 
# with already set with newly 2 
print("8 powerof 5 = ", base(8))

# lambda functions inside map() and filter() 
    
a = [100, 2, 8, 60, 5, 4, 3, 31, 10, 11] 
  
# in filter either we use assignment or conditional operator, the pass actual parameter will get return 

filtered = filter (lambda x: x % 2 == 0, a)  
print(list(filtered)) 
  
# in map either we use assignment or conditional operator, the result of the value will get returned 

maped = map (lambda x: x % 2 == 0, a)  
print(list(maped))

# Global and Local Variables in Python
# This function uses global variable s 

def f():  
    print(s)  
  
# Global scope 

s = "I love Geeksforgeeks"
f()

# name same as s. 

def f():  
    s = "Me too."
    print(s)  
  
# Global scope 

s = "I love Geeksforgeeks" 
f() 
print(s)

# This function modifies the global variable 's' 

def f(): 
    global s 
    print(s) 
    s = "Look for Geeksforgeeks Python Section"
    print(s)  
  
# Global Scope 

s = "Python is great!" 
f() 
print(s)

a = 1
  
# Uses global because there is no local 'a' 

def f(): 
    print('Inside f() :'),a 
  
# Variable 'a' is redefined as a local 

def g():     
    a = 2
    print('Inside g() : '),a 
  
# Uses global keyword to modify global 'a' 

def h():     
    global a 
    a = 3
    print('Inside h() : '),a 
  
# Global scope 

print('global : '),a 
f() 
print('global : '),a 
g() 
print('global : '),a 
h() 
print('global : '),a

# Global keyword in Python
# use global keyword for accessing a global value 
# global variable 

a = 15
b = 10
  
# function to perform addition 

def add(): 
    c = a + b 
    print(c) 
  
# calling a function 

add()

# # a global value without using global keyword   
# a = 15  
# # function to change a global value 

# def change():  
#     # increment value of a by 5 
#     a = a + 5 
#     print(a) 
  
# change()

# value inside a function 
  
x = 15
def change(): 
  
    # using a global keyword 
    
    global x 
  
    # increment value of a by 5 
    
    x = x + 5 
    print("Value of x inside a function :", x) 

change() 
print("Value of x outside a function :", x)

# Global variables across python modules : https://www.geeksforgeeks.org/global-keyword-in-python/?ref=lbp
# global in nested function 
  
def add(): 
     x = 15
       
     def change(): 
         global x 
         x = 20
     print("Before making changing: ", x) 
     print("Making change") 
     change() 
     print("After making change: ", x) 
  
add() 
print("value of x",x)

# First Class functions in Python
# Python program to illustrate functions can be treated as objects 

def shout(text): 
    return text.upper() 
  
print(shout('Hello')) 
  
yell = shout 
  
print(yell('Hello'))

# can be passed as arguments to other functions 

def shout(text): 
    return text.upper() 
  
def whisper(text): 
    return text.lower() 
  
def greet(func): 
    # storing the function in a variable 
    greeting = func("Hi, I am created by a function passed as an argument.") 
    print(greeting)  
  
greet(shout) 
greet(whisper)

# Functions can return another function 
  
def create_adder(x): 
    def adder(y): 
        return x+y 
  
    return adder 
  
add_15 = create_adder(15) 
  
print(add_15(10))









































































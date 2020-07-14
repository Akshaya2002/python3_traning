# Ternary Operator in Python
# Syntax :[on_true] if [expression] else [on_false] 

# Program to demonstrate conditional operator 
a, b = 10, 20
  
# Copy value of a in min if a < b else copy b 
min = a if a < b else b 
  
print(min) 

# Direct Method by using tuples, Dictionary and lambda

a, b = 10, 20
  
# Use tuple for selecting an item 
# (if_test_false,if_test_true)[test] 
print( (b, a) [a < b] ) 
  
# Use Dictionary for selecting an item 
print({True: a, False: b} [a < b]) 
  
# lamda is more efficient than above two methods 
# because in lambda  we are assure that 
# only one expression will be evaluated unlike in 
# tuple and Dictionary 
print((lambda: b, lambda: a)[a < b]()) 

# Ternary operator can be written as nested if-else

a, b = 10, 20
  
if a != b: 
    if a > b: 
        print("a is greater than b") 
    else: 
        print("b is greater than a") 
else: 
    print("Both a and b are equal") 
    
# (or)
    
a, b = 10, 20
  
print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a") 

# Division Operators in Python

# "/" for both integers and floating points

print (5/2)
print (-5/2)
print (5.0/2)
print (-5.0/2)

# Python Operator Overloading ----> https://www.programiz.com/python-programming/operator-overloading

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y


# p1 = Point(1, 2)
# p2 = Point(2, 3)
# print(p1+p2)

# TypeError was raised, since Python didn't know how to add two Point objects together

# Python Special Functions

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


p1 = Point(2, 3)
print(p1)

# Overloading the + Operator

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1+p2)

# Overloading Comparison Operators

# overloading the less than operator
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag

p1 = Point(1,1)
p2 = Point(-2,-3)
p3 = Point(1,-1)

# use less than
print(p1<p2)
print(p2<p3)
print(p1<p3)

# Python any() and all() function ---> The syntax of any() is: any(iterable) and The syntax of all() is: all(iterable)
# iterable -----> list, string, dictionary etc.

# Example 1: Using any() and all() on Python Lists ---> instead of any need to put all

# True since 1,3 and 4 (at least one) is true
l = [1, 3, 4, 0]
print(any(l))

# False since both are False
l = [0, False]
print(any(l))

# True since 5 is true
l = [0, False, 5]
print(any(l))

# False since iterable is empty
l = []
print(any(l))

# Example 2: Using any() and all() on Python Strings

# Atleast one (in fact all) elements are True
s = "This is good"
print(any(s))

# 0 is False
# '0' is True since its a string character
s = '000'
print(any(s))

# False since empty iterable
s = ''
print(any(s))

# Example 3: Using any() and all() with Python Dictionaries

# 0 is False
d = {0: 'False'}
print(any(d))

# 1 is True
d = {0: 'False', 1: 'True'}
print(any(d))

# 0 and False are false
d = {0: 'False', False: 0}
print(any(d))

# iterable is empty
d = {}
print(any(d))

# 0 is False
# '0' is True
d = {'0': 'False'}
print(any(d))

















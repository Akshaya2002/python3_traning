# 1. Keywords in python

import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# None keyword example 

def a_void_function():
    a = 1
    b = 2
    c = a + b

x = a_void_function()
print(x)

# Yield keyword example

def generator():
    for i in range(6):
        yield i*i

g = generator()
for i in g:
    print(i)
    
with open('example.txt', 'w') as my_file:
    my_file.write('Hello world!')
    
# return keyword example
    
def func_return():
    a = 10
    return a

def no_return():
    a = 10

print(func_return())
print(no_return())

# non local keyword example

def outer_function():
    a = 5
    def inner_function():
        nonlocal a
        a = 10
        print("Inner function: ",a)
    inner_function()
    print("Outer function: ",a)

outer_function()

# lambda keyword example

a = lambda x: x*2
for i in range(1,6):
    print(a(i))
    
# global keyword example
    
globvar = 10
def read1():
    print(globvar)
def write1():
    global globvar
    globvar = 5
def write2():
    globvar = 15

read1()
write1()
read1()
write2()
read1()

# except,raise and try keyword example

def reciprocal(num):
    try:
        r = 1/num
    except:
        print('Exception caught')
        return
    return r

print(reciprocal(10))
print(reciprocal(0))

# async and await keyword example

import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('world')
    
# as keyword example
    
import math as myAlias

myAlias.cos(myAlias.pi)

# 2. Namespace and scopes in python

def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a =', a)

# Python indentation example

for i in range(1,11):
    print(i)
    if i == 5:
        break
    
# Python multi line statement example
        
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
    
# () [] {} ---> we can use in python statements
    
a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)

colors = ['red',
          'blue',
          'green']

a = 1; b = 2; c = 3

# Indentation can be ignored in line continuation

if True:
    print('Hello')
    a = 5
    
if True: print('Hello'); a = 5

# Docstrings in Python

def double(num):
    """Function to double the value"""
    return 2*num
print(double.__doc__)

# Input/Output in python

# 1.Python Output Using print() function

print('This sentence is output to the screen')

# actual syntax of print function
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='&')

# Output formatting ---> str.format() method example

x = 5; y = 10
print('The value of x is {} and y is {}'.format(x,y))

print('I love {0} and {1}'.format('bread','butter'))
print('I love {1} and {0}'.format('bread','butter'))

# also format strings like the old sprintf()

x = 12.3456789
print('The value of x is %3.2f' %x)

# 2.Python Input ---> The syntax for input() is: input([prompt])

num = input('Enter a number: ')

int('10')

# Python Import

import math
print(math.pi)

















    
    
    



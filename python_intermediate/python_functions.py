# Functions in Python(A simple Python function to check whether x is even or odd)

def evenOdd( x ): 
    
    if (x % 2 == 0): 
        print("even")
    else: 
        print("odd")
  
# Driver code 

evenOdd(2) 
evenOdd(3)

# Pass by Reference or pass by value
# Here x is a new reference to same list lst 

def myFun(x): 
   x[0] = 20
  
# Driver Code(Note that lst is modified after function call) 

lst = [10, 11, 12, 13, 14, 15]  
myFun(lst); 
print(lst)

def myFun(x): 
  
# After below line link of x with previous object gets broken. A new object is assigned to x. 

    x = [20, 30, 40] 
  
# Driver Code(Note that lst is not modified after function call) 

lst = [10, 11, 12, 13, 14, 15]  
myFun(lst); 
print(lst)

def swap(x, y): 
    temp = x; 
    x = y; 
    y = temp; 
  
# Driver code 
x = 2
y = 3
swap(x, y) 
print(x) 
print(y)

# Default arguments

def myFun(x, y=50): 
    print("x: ", x) 
    print("y: ", y) 
  
# Driver code (We call myFun() with only 
# argument) 

myFun(10)

# Keyword arguments

def student(firstname, lastname):  
     print(firstname, lastname)      
    
# Keyword arguments                   

student(firstname ='Geeks', lastname ='Practice')     
student(lastname ='Practice', firstname ='Geeks')

# *args and **kwargs in Python
# *args for variable number of arguments 

def myFun(*argv):  
    for arg in argv:  
        print (arg) 
    
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# *args with first extra argument 

def myFun(arg1, *argv): 
    print ("First argument :", arg1) 
    for arg in argv: 
        print("Next argument through *argv :", arg) 
  
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# *kargs for variable number of keyword arguments 
  
def myFun(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
# Driver code 
myFun(first ='Geeks', mid ='for', last='Geeks')

# variable number of keyword arguments with one extra argument. 
  
def myFun(arg1, **kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
# Driver code 
myFun("Hi", first ='Geeks', mid ='for', last='Geeks')

# Using *args and **kwargs to call a function

def myFun(arg1, arg2, arg3): 
    print("arg1:", arg1) 
    print("arg2:", arg2) 
    print("arg3:", arg3) 
      
# Now we can use *args or **kwargs to pass arguments to this function :  

args = ("Geeks", "for", "Geeks") 
myFun(*args) 
  
kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"} 
myFun(**kwargs)

# Using *args and **kwargs in same line to call a function

def myFun(*args,**kwargs): 
    print("args: ", args) 
    print("kwargs: ", kwargs)   
  
# Now we can use both *args ,**kwargs to pass arguments to this function : 

myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")

# When to use yield instead of return in Python?
# A generator function that yields 1 for the first time,2 second time and 3 third time 

def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
  
# Driver code to check above generator function 

for value in simpleGeneratorFun():  
    print(value)

# A Python program to generate squares from 1 to 100 using yield and therefore generator 
# An infinite generator function that prints 
# next square number. It starts with 1 

def nextSquare(): 
    i = 1; 
  
    # An Infinite loop to generate squares  
   
    while True: 
        yield i*i                 
        i += 1  # Next execution resumes  
                # from this point      
  
# Driver code to test above generator function 

for num in nextSquare(): 
    if num > 100: 
         break    
    print(num)

# Generators in Python    
# A generator function that yields 1 for first time,2 second time and 3 third time 

def simpleGeneratorFun(): 
    yield 1            
    yield 2            
    yield 3            
   
# Driver code to check above generator function 
for value in simpleGeneratorFun():  
    print(value)

# A Python program to demonstrate use of generator object with next()  
# A generator function 
# def simpleGeneratorFun(): 
#     yield 1
#     yield 2
#     yield 3
   
# x is a generator object 
# x = simpleGeneratorFun() 
  
# Iterating over the generator object using next 
# print(x.next()) # In Python 3, __next__() 
# print(x.next()) 
# print(x.next())

# A simple generator for Fibonacci Numbers 
# def fib(limit): 
      
#     # Initialize first two Fibonacci Numbers  
#     a, b = 0, 1
  
#     # One by one yield next Fibonacci Number 
#     while a < limit: 
#         yield a 
#         a, b = b, a + b 
  
# # Create a generator object 
# x = fib(5) 
  
# # Iterating over the generator object using next 
# print(x.next()) # In Python 3, __next__() 
# print(x.next()) 
# print(x.next()) 
# print(x.next()) 
# print(x.next()) 
  
# # Iterating over the generator object using for 
# # in loop. 
# print("\nUsing for in loop") 
# for i in fib(5):  
#     print(i)

































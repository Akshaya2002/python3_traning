# Python Closures Nested functions in Python
# nested functions 

def outerFunction(text): 
    text = text 
  
    def innerFunction(): 
        print(text) 
  
    innerFunction() 
  
if __name__ == '__main__': 
    outerFunction('Hey!')
    
# closures 

def outerFunction(text): 
    text = text 
  
    def innerFunction(): 
        print(text) 
  
    return innerFunction # Note we are returning function WITHOUT parenthesis 
  
if __name__ == '__main__': 
    myFunction = outerFunction('Hey!') 
    myFunction()
    
# closures 

import logging 
logging.basicConfig(filename='example.log', level=logging.INFO) 
  
  
def logger(func): 
    def log_func(*args): 
        logging.info( 
            'Running "{}" with arguments {}'.format(func.__name__, args)) 
        print(func(*args)) 
    # Necessary for closure to work (returning WITHOUT parenthesis) 
    return log_func               
  
def add(x, y): 
    return x+y 
  
def sub(x, y): 
    return x-y 
  
add_logger = logger(add) 
sub_logger = logger(sub) 
  
add_logger(3, 3) 
add_logger(4, 5) 
  
sub_logger(10, 5) 
sub_logger(20, 10)   
    
# Decorators in Python Syntax for Decorator: def hello_decorator(): print("Gfg")
# defining a decorator 

def hello_decorator(func): 

	# inner1 is a Wrapper function in which the argument is called 	
	# inner function can access the outer local functions like in this case "func" 
	def inner1(): 
		print("Hello, this is before function execution") 

		# calling the actual function now inside the wrapper function. 
		func() 

		print("This is after function execution") 
		
	return inner1 


# defining a function, to be called inside wrapper 
def function_to_be_used(): 
	print("This is inside the function !!") 


# passing 'function_to_be_used' inside the decorator to control its behavior 
function_to_be_used = hello_decorator(function_to_be_used) 


# calling the function 
function_to_be_used() 
 
# importing libraries 
import time 
import math 

# decorator to calculate duration 
# taken by any function. 
def calculate_time(func): 
	
	# added arguments inside the inner1, 
	# if function takes any arguments, 
	# can be added like this. 
	def inner1(*args, **kwargs): 

		# storing time before function execution 
		begin = time.time() 
		
		func(*args, **kwargs) 

		# storing time after function execution 
		end = time.time() 
		print("Total time taken in : ", func.__name__, end - begin) 

	return inner1 



# this can be added to any function present, 
# in this case to calculate a factorial 
@calculate_time
def factorial(num): 

	# sleep 2 seconds because it takes very less time 
	# so that you can see the actual difference 
	time.sleep(2) 
	print(math.factorial(num)) 

# calling the function. 
factorial(10) 

def hello_decorator(func): 
	def inner1(*args, **kwargs): 
		
		print("before Execution") 
		
		# getting the returned value 
		returned_value = func(*args, **kwargs) 
		print("after Execution") 
		
		# returning the value to the original frame 
		return returned_value 
		
	return inner1 


# adding decorator to the function 
@hello_decorator
def sum_two_numbers(a, b): 
	print("Inside the function") 
	return a + b 

a, b = 1, 2

# getting the value through return of the function 
print("Sum =", sum_two_numbers(a, b)) 

# Decorators with parameters in Python Syntax for decorators with parameters –
# @decorator(params)
# def func_name():
#     ''' Function implementation'''

# Decorators basic in Python  
  
def decorator_fun(func):  
  print("Inside decorator")  
  
  def inner(*args, **kwargs):  
    print("Inside inner function")  
    print("Decorated the function")  
    # do operations with func 
      
    func() 
      
  return inner  
  
@decorator_fun
def func_to():  
    print("Inside actual function")  
  
func_to()

# Decorators with parameters in Python  
  
def decorator_fun(func):  
  print("Inside decorator")  
  
  def inner(*args, **kwargs):  
    print("Inside inner function")  
    print("Decorated the function")  
      
    func() 
      
  return inner  
  
  
def func_to():  
    print("Inside actual function")  
  
# another way of using decorators 
decorator_fun(func_to)()

# Decorators with parameters in Python  
  
def decorator(*args, **kwargs): 
    print("Inside decorator") 
      
    def inner(func): 
          
        # code functionality here 
        print("Inside inner function") 
        print("I like", kwargs['like'])  
          
        func() 
          
    # reurning inner function     
    return inner 
  
@decorator(like = "geeksforgeeks") 
def my_func(): 
    print("Inside actual function")
    
# Decorators with parameters in Python  
  
def decorator_func(x, y): 
  
    def Inner(func): 
  
        def wrapper(*args, **kwargs): 
            print("I like Geeksforgeeks") 
            print("Summation of values - {}".format(x+y) ) 
  
            func(*args, **kwargs) 
              
        return wrapper 
    return Inner 
  
  
# Not using decorator  
def my_fun(*args): 
    for ele in args: 
        print(ele) 
  
# another way of using dacorators 
decorator_func(12, 15)(my_fun)('Geeks', 'for', 'Geeks')

# Memoization using decorators in Python
# Simple recursive program to find factorial 

def facto(num): 
    if num == 1: 
        return 1
    else: 
        return num * facto(num-1) 
          
  
print(facto(5))

# Factorial program with memoization using 
# decorators. 
  
# A decorator function for function 'f' passed 
# as parameter 
def memoize_factorial(f): 
    memory = {} 
  
    # This inner function has access to memory 
    # and 'f' 
    def inner(num): 
        if num not in memory:          
            memory[num] = f(num) 
        return memory[num] 
  
    return inner 
      
@memoize_factorial
def facto(num): 
    if num == 1: 
        return 1
    else: 
        return num * facto(num-1) 
  
print(facto(5))


 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
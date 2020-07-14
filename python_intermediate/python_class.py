# Python Classes and Objects

class Dog:  
      
    # A simple class 
    # attribute 
    attr1 = "mamal"
    attr2 = "dog"
  
    # A sample method   
    def fun(self):  
        print("I'm a", self.attr1) 
        print("I'm a", self.attr2) 
  
# Driver code 
# Object instantiation 
Rodger = Dog() 
  
# Accessing class attributes 
# and method through objects 
print(Rodger.attr1) 
Rodger.fun()

# A Sample class with init method  
class Person:  
    
    # init method or constructor   
    def __init__(self, name):  
        self.name = name  
    
    # Sample Method   
    def say_hi(self):  
        print('Hello, my name is', self.name)  
    
p = Person('Nikhil')  
p.say_hi()

# Python program to show that the variables with a value   
# assigned in the class declaration, are class variables and  
# variables inside methods and constructors are instance  
# variables.  
     
# Class for Dog  
class Dog:  
    
    # Class Variable  
    animal = 'dog'             
    
    # The init method or constructor  
    def __init__(self, breed, color):  
      
        # Instance Variable      
        self.breed = breed 
        self.color = color         
     
# Objects of Dog class  
Rodger = Dog("Pug", "brown")  
Buzo = Dog("Bulldog", "black")  
  
print('Rodger details:')    
print('Rodger is a', Rodger.animal)  
print('Breed: ', Rodger.breed) 
print('Color: ', Rodger.color) 
  
print('\nBuzo details:')    
print('Buzo is a', Buzo.animal)  
print('Breed: ', Buzo.breed) 
print('Color: ', Buzo.color) 
  
# Class variables can be accessed using class  
# name also  
print("\nAccessing class variable using class name") 
print(Dog.animal)

# instance variables inside methods  
     
# Class for Dog  
class Dog:  
        
    # Class Variable  
    animal = 'dog'      
        
    # The init method or constructor  
    def __init__(self, breed):  
            
        # Instance Variable  
        self.breed = breed              
    
    # Adds an instance variable   
    def setColor(self, color):  
        self.color = color  
        
    # Retrieves instance variable      
    def getColor(self):      
        return self.color     
    
# Driver Code  
Rodger = Dog("pug")  
Rodger.setColor("brown")  
print(Rodger.getColor())

# Constructors in Python Syntax of constructor declaration : def __init__(self): body of the constructor

class GeekforGeeks: 
  
    # default constructor 
    def __init__(self): 
        self.geek = "GeekforGeeks"
  
    # a method for printing data members 
    def print_Geek(self): 
        print(self.geek) 
  
  
# creating object of the class 
obj = GeekforGeeks() 
  
# calling the instance method using the object obj 
obj.print_Geek()

class Addition: 
    first = 0
    second = 0
    answer = 0
      
    # parameterized constructor 
    def __init__(self, f, s): 
        self.first = f 
        self.second = s 
      
    def display(self): 
        print("First number = " + str(self.first)) 
        print("Second number = " + str(self.second)) 
        print("Addition of two numbers = " + str(self.answer)) 
  
    def calculate(self): 
        self.answer = self.first + self.second 
  
# creating object of the class 
# this will invoke parameterized constructor 
obj = Addition(1000, 2000) 
  
# perform Addition 
obj.calculate() 
  
# display result 
obj.display()

# Destructors in Python Syntax of destructor declaration : def __del__(self): body of destructor

class Employee: 
  
    # Initializing 
    def __init__(self): 
        print('Employee created.') 
  
    # Deleting (Calling destructor) 
    def __del__(self): 
        print('Destructor called, Employee deleted.') 
  
obj = Employee() 
del obj 

class Employee: 
  
    # Initializing  
    def __init__(self): 
        print('Employee created') 
  
    # Calling destructor 
    def __del__(self): 
        print("Destructor called") 
  
def Create_obj(): 
    print('Making Object...') 
    obj = Employee() 
    print('function end...') 
    return obj 
  
print('Calling Create_obj() function...') 
obj = Create_obj() 
print('Program End...')

class A: 
    def __init__(self, bb): 
        self.b = bb 
  
class B: 
    def __init__(self): 
        self.a = A(self) 
    def __del__(self): 
        print("die") 
  
def fun(): 
    b = B() 
  
fun()

# Inheritance in Python
# Base or Super class. Note object in bracket. 
# (Generally, object is made ancestor of all classes) 
# In Python 3.x "class Person" is  
# equivalent to "class Person(object)" 

class Person(object): 
       
    # Constructor 
    def __init__(self, name): 
        self.name = name 
   
    # To get name 
    def getName(self): 
        return self.name 
   
    # To check if this person is an employee 
    def isEmployee(self): 
        return False
   
   
# Inherited or Subclass (Note Person in bracket) 
class Employee(Person): 
   
    # Here we return true 
    def isEmployee(self): 
        return True
   
# Driver code 
emp = Person("Geek1")  # An Object of Person 
print(emp.getName(), emp.isEmployee()) 
   
emp = Employee("Geek2") # An Object of Employee 
print(emp.getName(), emp.isEmployee())

# # parent class 
# class Person( object ):	 

# 		# __init__ is known as the constructor		 
# 		def __init__(self, name, idnumber): 
# 				self.name = name 
# 				self.idnumber = idnumber 
# 		def display(self): 
# 				print(self.name) 
# 				print(self.idnumber) 

# # child class 
# class Employee( Person ):		 
# 		def __init__(self, name, idnumber, salary, post): 
# 				self.salary = salary 
# 				self.post = post 

# 				# invoking the __init__ of the parent class 
# 				Person.__init__(self, name, idnumber) 

# 				
# # creation of an object variable or an instance 
# a = Employee('Rahul', 886012)	 

# # calling a function of the class Person using its instance 
# a.display() 

# # forget to invoke __init__() of the parent. 
  
# class A: 
#       def __init__(self, n = 'Rahul'): 
#               self.name = n 
# class B(A): 
#       def __init__(self, roll): 
#               self.roll = roll 
  
# object = B(23) 
# print (object.name)

# Python example to show the working of multiple 
# inheritance 
class Base1(object): 
	def __init__(self): 
		self.str1 = "Geek1"
		print("Base1") 

class Base2(object): 
	def __init__(self): 
		self.str2 = "Geek2"		
		print("Base2") 

class Derived(Base1, Base2): 
	def __init__(self): 
		
		# Calling constructors of Base1 
		# and Base2 classes 
		Base1.__init__(self) 
		Base2.__init__(self) 
		print("Derived") 
		
	def printStrs(self): 
		print(self.str1, self.str2) 
		

ob = Derived() 
ob.printStrs() 

# Base or Super class. Note object in bracket. 
# (Generally, object is made ancestor of all classes) 
# In Python 3.x "class Person" is  
# equivalent to "class Person(object)" 
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

# Python program to demonstrate private members 
# of the parent class 
# class C(object): 
#        def __init__(self): 
#               self.c = 21
  
#               # d is private instance variable  
#               self.__d = 42    
# class D(C): 
#        def __init__(self): 
#               self.e = 84
#               C.__init__(self) 
# object1 = D() 
  
# # produces an error as d is private instance variable 
# print(object1.d)

# Types of inheritance Python
# Base class or Parent class 
class Child:  
  
    # Constructor 
    def __init__(self, name):  
        self.name = name  
  
    # To get name 
    def getName(self):  
        return self.name  
  
    # To check if this person is student  
    def isStudent(self):  
        return False
  
# Derived class or Child class 
class Student(Child): 
  
    # True is returned 
    def isStudent(self):  
        return True
  
   
# Driver code  
# An Object of Child  
std = Child("Ram") 
print(std.getName(), std.isStudent())  
  
# An Object of Student  
std = Student("Shivam")  
print(std.getName(), std.isStudent())

# Base class 
class Parent: 
     def func1(self): 
          print("This function is in parent class.") 
  
# Derived class 
class Child(Parent): 
     def func2(self): 
          print("This function is in child class.") 
  
# Driver's code 
object = Child() 
object.func1() 
object.func2()

# Base class1 
class Mother: 
    mothername = "" 
    def mother(self): 
        print(self.mothername) 
  
# Base class2 
class Father: 
    fathername = "" 
    def father(self): 
        print(self.fathername) 
  
# Derived class 
class Son(Mother, Father): 
    def parents(self): 
        print("Father :", self.fathername) 
        print("Mother :", self.mothername) 
  
# Driver's code 
s1 = Son() 
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()

# Base class 
class Grandfather: 
    grandfathername =""  
    def grandfather(self): 
        print(self.grandfathername) 
  
# Intermediate class 
class Father(Grandfather): 
    fathername = "" 
    def father(self): 
        print(self.fathername) 
  
# Derived class 
class Son(Father): 
    def parent(self): 
        print("GrandFather :", self.grandfathername) 
        print("Father :", self.fathername) 
  
# Driver's code 
s1 = Son() 
s1.grandfathername = "Srinivas"
s1.fathername = "Ankush"
s1.parent()

# Base class 
class Parent: 
      def func1(self): 
          print("This function is in parent class.") 
  
# Derived class1 
class Child1(Parent): 
      def func2(self): 
          print("This function is in child 1.") 
  
# Derivied class2 
class Child2(Parent): 
      def func3(self): 
          print("This function is in child 2.") 
   
# Driver's code 
object1 = Child1() 
object2 = Child2() 
object1.func1() 
object1.func2() 
object2.func1() 
object2.func3()

class School: 
     def func1(self): 
         print("This function is in school.") 
   
class Student1(School): 
     def func2(self): 
         print("This function is in student 1. ") 
   
class Student2(School): 
     def func3(self): 
         print("This function is in student 2.") 
   
class Student3(Student1, School): 
     def func4(self): 
         print("This function is in student 3.") 
   
# Driver's code 
object = Student3() 
object.func1() 
object.func2()

# Encapsulation in Python
# Creating a base class 
class Base: 
    def __init__(self): 
          
        # Protected member 
        self._a = 2
  
# Creating a derived class     
class Derived(Base): 
    def __init__(self): 
          
        # Calling constructor of 
        # Base class 
        Base.__init__(self)  
        print("Calling protected member of base class: ") 
        print(self._a) 
  
obj1 = Derived() 
          
obj2 = Base() 
  
# Calling protected member 
# Outside class will  result in  
# AttributeError 
print(obj2.a)

# Creating a Base class 
class Base: 
    def __init__(self): 
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
  
# Creating a derived class 
class Derived(Base): 
    def __init__(self): 
          
        # Calling constructor of 
        # Base class 
        Base.__init__(self)  
        print("Calling private member of base class: ") 
        print(self.__a) 
# Driver code 
obj1 = Base() 
print(obj1.a) 
  
# Uncommenting print(obj1.c) will 
# raise an AttributeError 
  
# Uncommenting obj2 = Derived() will 
# also raise an AtrributeError as 
# private member of base class  
# is called inside derived class

































































































































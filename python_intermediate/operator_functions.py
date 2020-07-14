# Operator Functions in Python | Set 1 ----> https://www.geeksforgeeks.org/operator-functions-python-set-2/?ref=lbp

# Python code to demonstrate working of  
# add(), sub(), mul() 
  
# importing operator module  
import operator 
  
# Initializing variables 
a = 4
  
b = 3
  
# using add() to add two numbers 
print ("The addition of numbers is :",end=""); 
print (operator.add(a, b)) 
  
# using sub() to subtract two numbers 
print ("The difference of numbers is :",end=""); 
print (operator.sub(a, b)) 
  
# using mul() to multiply two numbers 
print ("The product of numbers is :",end=""); 
print (operator.mul(a, b)) 

# Python code to demonstrate working of  
# truediv(), floordiv(), pow(), mod() 
  
# importing operator module  
import operator 
  
# Initializing variables 
a = 5
  
b = 2
  
# using truediv() to divide two numbers 
print ("The true division of numbers is : ",end=""); 
print (operator.truediv(a,b)) 
  
# using floordiv() to divide two numbers 
print ("The floor division of numbers is : ",end=""); 
print (operator.floordiv(a,b)) 
  
# using pow() to exponentiate two numbers 
print ("The exponentiation of numbers is : ",end=""); 
print (operator.pow(a,b)) 
  
# using mod() to take modulus of two numbers 
print ("The modulus of numbers is : ",end=""); 
print (operator.mod(a,b)) 

# Python code to demonstrate working of  
# lt(), le() and eq() 
  
# importing operator module  
import operator 
  
# Initializing variables 
a = 3
  
b = 3
  
# using lt() to check if a is less than b 
if(operator.lt(a,b)): 
       print ("3 is less than 3") 
else : print ("3 is not less than 3") 
  
# using le() to check if a is less than or equal to b 
if(operator.le(a,b)): 
       print ("3 is less than or equal to 3") 
else : print ("3 is not less than or equal to 3") 
  
# using eq() to check if a is equal to b 
if (operator.eq(a,b)): 
       print ("3 is equal to 3") 
else : print ("3 is not equal to 3") 

# Python code to demonstrate working of  
# gt(), ge() and ne() 
  
# importing operator module  
import operator 
  
# Initializing variables 
a = 4
  
b = 3
  
# using gt() to check if a is greater than b 
if (operator.gt(a,b)): 
       print ("4 is greater than 3") 
else : print ("4 is not greater than 3") 
  
# using ge() to check if a is greater than or equal to b 
if (operator.ge(a,b)): 
       print ("4 is greater than or equal to 3") 
else : print ("4 is not greater than or equal to 3") 
  
# using ne() to check if a is not equal to b 
if (operator.ne(a,b)): 
       print ("4 is not equal to 3") 
else : print ("4 is equal to 3") 

# Operator Functions in Python | Set 2

# Python code to demonstrate working of  
# setitem(), delitem() and getitem() 
  
# importing operator module  
import operator 
  
# Initializing list 
li = [1, 5, 6, 7, 8] 
  
# printing original list  
print ("The original list is : ",end="") 
for i in range(0,len(li)): 
    print (li[i],end=" ") 
  
print ("\r") 
  
# using setitem() to assign 3 at 4th position 
operator.setitem(li,3,3) 
  
# printing modified list after setitem() 
print ("The modified list after setitem() is : ",end="") 
for i in range(0,len(li)): 
    print (li[i],end=" ") 
  
print ("\r") 
  
# using delitem() to delete value at 2nd index 
operator.delitem(li,1) 
  
# printing modified list after delitem() 
print ("The modified list after delitem() is : ",end="") 
for i in range(0,len(li)): 
    print (li[i],end=" ") 
  
print ("\r") 
  
# using getitem() to access 4th element 
print ("The 4th element of list is : ",end="") 
print (operator.getitem(li,3)) 

# Python code to demonstrate working of  
# concat() and contains() 
  
# importing operator module  
import operator 
  
# Initializing string 1 
s1 = "geeksfor"
  
# Initializing string 2 
s2 = "geeks"
  
# using concat() to concatenate two strings 
print ("The concatenated string is : ",end="") 
print (operator.concat(s1,s2)) 
  
# using contains() to check if s1 contains s2 
if (operator.contains(s1,s2)): 
       print ("geeksfor contains geeks") 
else : print ("geeksfor does not contain geeks") 

# Python code to demonstrate working of  
# and_(), or_(), xor(), invert() 
  
# importing operator module  
import operator 
  
# Initializing a and b 
  
a = 1
  
b = 0
  
# using and_() to display bitwise and operation 
print ("The bitwise and of a and b is : ",end="") 
print (operator.and_(a,b)) 
  
# using or_() to display bitwise or operation 
print ("The bitwise or of a and b is : ",end="") 
print (operator.or_(a,b)) 
  
# using xor() to display bitwise exclusive or operation 
print ("The bitwise xor of a and b is : ",end="") 
print (operator.xor(a,b)) 
  
# using invert() to invert value of a 
operator.invert(a) 
  
# printing modified value 
print ("The inverted value of a is : ",end="") 
print (a) 








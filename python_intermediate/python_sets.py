# Python Sets ---> Creating a Set
 
set1 = set() 
print("Intial blank Set: ") 
print(set1) 
  
# Creating a Set with the use of a String 

set1 = set("GeeksForGeeks") 
print("\nSet with the use of String: ") 
print(set1) 
  
# Creating a Set with the use of Constructor(Using object to Store String) 

String = 'GeeksForGeeks'
set1 = set(String) 
print("\nSet with the use of an Object: " ) 
print(set1) 
  
# Creating a Set with the use of a List 

set1 = set(["Geeks", "For", "Geeks"]) 
print("\nSet with the use of List: ") 
print(set1)

# Creating a Set with a List of Numbers(Having duplicate values) 

set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5]) 
print("\nSet with the use of Numbers: ") 
print(set1) 
  
# Creating a Set with a mixed type of values(Having numbers and strings) 

set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks']) 
print("\nSet with the use of Mixed Values") 
print(set1) 

# Adding Elements to a Set ---> Using add() method

# Creating a Set 

set1 = set() 
print("Intial blank Set: ") 
print(set1) 
  
# Adding element and tuple to the Set 

set1.add(8) 
set1.add(9) 
set1.add((6,7)) 
print("\nSet after Addition of Three elements: ") 
print(set1) 
  
# Adding elements to the Set using Iterator 

for i in range(1, 6): 
    set1.add(i) 
print("\nSet after Addition of elements from 1-5: ") 
print(set1)

# Using update() method

# Addition of elements to the Set using Update function 

set1 = set([ 4, 5, (6, 7)]) 
set1.update([10, 11]) 
print("\nSet after Addition of elements using Update: ") 
print(set1)

# Accessing a Set ---> Creating a set 

set1 = set(["Geeks", "For", "Geeks"]) 
print("\nInitial set") 
print(set1) 
  
# Accessing element using for loop 

print("\nElements of set: ") 
for i in set1: 
    print(i, end=" ") 
  
# Checking the element using in keyword 

print("Geeks" in set1)

# Removing elements from the Set Using remove() method or discard() method

# Creating a Set 

set1 = set([1, 2, 3, 4, 5, 6,  
            7, 8, 9, 10, 11, 12]) 
print("Intial Set: ") 
print(set1) 
  
# Removing elements from Set using Remove() method 

set1.remove(5) 
set1.remove(6) 
print("\nSet after Removal of two elements: ") 
print(set1) 
  
# Removing elements from Set using Discard() method 

set1.discard(8) 
set1.discard(9) 
print("\nSet after Discarding two elements: ") 
print(set1) 
  
# Removing elements from Set using iterator method 

for i in range(1, 5): 
    set1.remove(i) 
print("\nSet after Removing a range of elements: ") 
print(set1) 

# Using pop() method ---> Creating a Set 

set1 = set([1, 2, 3, 4, 5, 6,  
            7, 8, 9, 10, 11, 12]) 
print("Intial Set: ") 
print(set1) 
  
# Removing element from the Set using the pop() method 

set1.pop() 
print("\nSet after popping an element: ") 
print(set1)

# Using clear() method ---> Creating a set 

set1 = set([1,2,3,4,5]) 
print("\n Initial set: ") 
print(set1)   
  
# Removing all the elements from Set using clear() method 

set1.clear() 
print("\nSet after clearing all the elements: ") 
print(set1)

# Frozen sets in Python ---> Creating a Set 

String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r') 
  
Fset1 = frozenset(String) 
print("The FrozenSet is: ") 
print(Fset1) 
  
# To print Empty Frozen Set No parameter is passed 

print("\nEmpty FrozenSet: ") 
print(frozenset())










































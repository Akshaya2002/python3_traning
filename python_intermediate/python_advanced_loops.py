# Python break statement 

s = 'geeksforgeeks'

# Using for loop 

for letter in s: 
  
    print(letter) 
    
    # break the loop as soon it sees 'e' 
    # or 's' 
    
    if letter == 'e' or letter == 's': 
        break
  
print("Out of for loop") 
print() 
  
i = 0
  
# Using while loop 

while True: 
    print(s[i]) 
  
    # break the loop as soon it sees 'e' 
    # or 's' 
    
    if s[i] == 'e' or s[i] == 's': 
        break
    i += 1
  
print("Out of while loop")

# Python Continue Statement
# loop from 1 to 10 

for i in range(1, 11): 
  
    # If i is equals to 6, continue to next iteration without printing  
    
    if i == 6: 
        continue
    else: 
       
        # otherwise print the value of i 
        
        print(i, end = " ") 

# Python pass Statement
        
li =['a', 'b', 'c', 'd'] 
  
for i in li: 
    
    if(i =='a'): 
        pass 
    else: 
        print(i)
     
# Looping Techniques in Python
# python code to demonstrate working of enumerate() 
  
for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']): 
    print(key, value) 
    
# python code to demonstrate working of zip() 
# initializing list 

questions = ['name', 'colour', 'shape'] 
answers = ['apple', 'red', 'a circle'] 
  
# using zip() to combine two containers and print values 

for question, answer in zip(questions, answers): 
    print('What is your {0}?  I am {1}.'.format(question, answer))

# python code to demonstrate working of iteritems(),items() 
  
d = { "geeks" : "for", "only" : "geeks" } 
  
# using iteritems to print the dictionary key-value pair 

print ("The key value pair using iteritems is : ") 
# for i,j in d.iteritems(): 
#     print(i,j) 
      
# using items to print the dictionary key-value pair 

# print ("The key value pair using items is : ")
# for i,j in d.items(): 
#     print(i,j) 
    
# python code to demonstrate working of items() 
  
king = {'Akbar': 'The Great', 'Chandragupta': 'The Maurya',  
        'Modi' : 'The Changer'} 
  
# using items to print the dictionary key-value pair 

for key, value in king.items(): 
    print(key, value)

# python code to demonstrate working of sorted() 
# initializing list 

lis = [ 1 , 3, 5, 6, 2, 1, 3 ] 
  
# using sorted() to print the list in sorted order 

print ("The list in sorted order is : ") 

for i in sorted(lis) : 
    print (i,end=" ") 
      
print ("\r") 
      
# using sorted() and set() to print the list in sorted order 
# use of set() removes duplicates. 

print ("The list in sorted order (without duplicates) is : ") 

for i in sorted(set(lis)) : 
    print (i,end=" ") 

# python code to demonstrate working of sorted() 
# initializing list 

basket = ['guave', 'orange', 'apple', 'pear',  
          'guava', 'banana', 'grape'] 
  
# using sorted() and set() to print the list in sorted order 

for fruit in sorted(set(basket)): 
    print(fruit) 

# python code to demonstrate working of reversed() 
# initializing list 

lis = [ 1 , 3, 5, 6, 2, 1, 3 ] 
  
  
# using revered() to print the list in reversed order 

print ("The list in reversed order is : ") 

for i in reversed(lis) : 
    print (i,end=" ")

# python code to demonstrate working of reversed() 
# using reversed() to print in reverse order 

for i in reversed(range(1, 10, 3)): 
    print (i)



































































































































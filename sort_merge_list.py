# creating a sorted merged list of 2 unsorted list in python

def sorted_list(list1,list2):
    final_list = list1 + list2
    final_list.sort()
    
    return(final_list)

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
print(sorted_list(list1, list2))
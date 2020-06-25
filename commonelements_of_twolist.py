# printing all common elements of twolist

def common_elements(list1,list2):
    list1_set = set(list1)
    list2_set = set(list2)
    
    if(list1_set & list2_set):
        print(list1_set & list2_set)
        
    else:
        print('no common elements')
        
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
common_elements(list1, list2)

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
common_elements(list1, list2)

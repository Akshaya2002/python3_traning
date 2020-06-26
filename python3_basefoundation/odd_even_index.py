
def oddnumberevennumber(num):
    oddindex = []
    evenindex = []
    
    for i in range(len(num)):
        
        if i % 2 == 0:
            oddindex.append(num[i])        
        else:
            evenindex.append(num[i])
            
    for i in sorted(oddindex):
        print(i,' ')
        
    for i in sorted(evenindex):
        print(i,' ')
        
num = [3,2,6,8,1,4,7]
oddnumberevennumber(num)

            
        
#converting string to a list

def Stringtolist(string):
    li = list(string.split(' '))
    return li

myString = 'My name is Akshaya'
print(Stringtolist(myString))
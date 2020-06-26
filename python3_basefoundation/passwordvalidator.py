import re
myPassword = 'Aks@1234'
flag = 0

while True:
    if(len(myPassword)<8):
        flag = -1
        break
    elif not re.search('[a-z]', myPassword):
        flag = -1
        break
    elif not re.search('[A-Z]', myPassword):
        flag = -1
        break
    elif not re.search('[0-9]', myPassword):
        flag = -1
        break
    elif not re.search('[_@$]', myPassword):
        flag = -1
        break
    else:
        flag = 0
        print('validpassword')
        break
    
if flag== -1:
    print('notvalidpassword')
    
    
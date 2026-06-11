n = int(input('ENTER A NUMBER - ')) #7
flag = True
for i in range(2,n):
    if n%i==0:
        flag = False
        break
    
if flag==True:        
    print('PRIME NUMBER')
else:
    print("NOT A PRIME NUMBER")
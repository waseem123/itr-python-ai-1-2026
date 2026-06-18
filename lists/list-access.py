mylist = ['Samsung','iPhone','Nokia','OnePlus','Vivo','Oppo','Vivo','Redmi','Vivo','Realme','Nothing']
print(mylist)

for i in mylist:
    print(i)
    
print(mylist[0])
print(mylist[4])
print('--------------------')

for i in range(0,len(mylist)):
    print(f'{i} -> {mylist[i]}')


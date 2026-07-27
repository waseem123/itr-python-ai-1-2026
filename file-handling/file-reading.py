myfile = open('demo.txt')
data = myfile.read()
print(data)
myfile.close()
print('------------------------')

myfile = open('demo.txt')
print(myfile.readline(10))
print(myfile.readline(30))
print(myfile.readline())
myfile.close()
print('------------------------')

myfile = open('demo.txt')
for i in myfile:
    print(i)
myfile.close()
print('------------------------')



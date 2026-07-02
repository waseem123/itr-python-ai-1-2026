class Person:
    name = 'Sam'
    city = 'California'
    age = 25
        
p1 = Person()
p2 = Person()
print(p1)
print(p2)
print('------------------')

print(p1.name)
print(p1.city)
print(p1.age)
print('------------------')


print(p2.name)
print(p2.city)
print(p2.age)
print('------------------')

p1.name = 'Alice'
p1.city = 'Paris'
p1.age = 21

print(p1.name)
print(p1.city)
print(p1.age)
print('------------------')
print(p2.name)
print(p2.city)
print(p2.age)
print('------------------')
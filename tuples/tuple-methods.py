mytuple = ('Blue','Black','Orange','Red','Green','Yellow','Black','Magenta','Dark Yellow',)
print(mytuple)

print(mytuple.count('Black'))
print(mytuple.index('Black'))

t1 = (10,20,30)
t2 = (100,200,300)
t3 = (1,2,3)

t = (t1,t2,t3)
print(t)

x = ((10, 20, 30), (100, 200, 300), (1, 2, 3))
print(x[0])

print(x[0][0])

for i in x:
    for j in i:
        print(j)
import random as r

print(r.randint(1,6))
print(r.randrange(1000,10000))

mylist = ['C','Mathematics','Java']
print(r.choice(mylist))

r.shuffle(mylist)
print(mylist)
list1 = ['C','C++','Java']
list2 = ['Python','c#','Javascript', 'C++']

list3 = list1 + list2
print(list3)

list2.extend(list1)
print(list1)
print(list2)

print(list1*20)

list1.reverse()
print(list1)


print(list2)
list2.sort(reverse=True)
print(list2)

print(list2.count('C++'))
print(list2.index('C++'))
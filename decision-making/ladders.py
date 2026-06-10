n1 = 20000
n2 = 2000
n3 = 20000

if n1>n2 and n1>n3:
    print(f'{n1} IS LARGER THAN {n2} AND {n3}')
elif n2>n1 and n2>n3:
    print(f'{n2} IS LARGER THAN {n1} AND {n3}')
elif n3>n1 and n3>n2:
    print(f'{n3} IS LARGER THAN {n1} AND {n2}')
else:
    print('ALL NUMBERS ARE EQUAL')
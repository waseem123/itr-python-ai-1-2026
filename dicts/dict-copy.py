emp1 = {
        'empId':101,
        'empDept':'Sales',
        'empSalary':50000
    }

print(emp1)

data = emp1
print(data)
print('----------------------')
data['empSalary'] = 95000
print(data)
print(emp1)

# x = 25
# y = x
# print(x,y)
# y = 3000
# print(x,y)

print('_____________________________________')
empdata = emp1.copy()
print(empdata)

empdata['empSalary'] = 55000
print(empdata)
print(emp1)
employees = {
    'emp1':{
        'empId':101,
        'empDept':'Sales'
    },
    'emp2':{
        'empId':102,
        'empDept':'Marketing'
    },
    'emp3':{
        'empId':103,
        'empDept':'HR'
    },
    'emp4':{
        'empId':104,
        'empDept':'Engineering'
    },
}
print(employees)

print(employees['emp3']['empDept'])

for i,j in employees['emp3'].items():
    print(j)
    

emp1={
        'empId':101,
        'empDept':'Sales'
    }

emp2={
        'empId':102,
        'empDept':'Marketing'
    }

emp3={
        'empId':103,
        'empDept':'HR'
    }

emp4={
        'empId':104,
        'empDept':'Engineering'
    }


empData = {
    'e1':emp1,
    'e2':emp2,
    'e3':emp3,
    'e4':emp4
}

print(empData)
mydict = {
            'name': 'alex', 
            'salary': 84000, 
            'job_role': 'Team Lead', 
            'department': 'AI', 
            'job_mode': 'WFH', 
            'experience': '5 Years', 
            'city': 'Bengaluru'
        }

print(mydict)

mydict.pop('department')
print(mydict)

mydict.popitem()
print(mydict)

del mydict['job_role']
print(mydict)

mydict.clear()
print(mydict)

del mydict
print(mydict)
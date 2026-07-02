mydict = {
            'name': 'alex', 
            'salary': 84000, 
            'job_role': 'Team Lead', 
            'department': 'AI', 
            'job_mode': 'WFH', 
            'experience': '5 Years', 
            'city': 'Bengaluru',
            'city':'Solapur',
            'mobileno':[9096288255,9096288256]
        }

print(mydict.keys())
print(mydict.values())
print(mydict.items())
print('---------------------------------------')

for i in mydict.keys():
    print(i,'-',mydict[i])
print("_________________________")    
for i in mydict.values():
    print(i)
print("_________________________")    

for i,j in mydict.items():
    print(i,'-',j)
    
print('-+++++++++++++++--')

print(mydict['mobileno'][1])
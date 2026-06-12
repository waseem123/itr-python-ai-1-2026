def showData(name='NA',city='NA'):
    print(f'My name is {name}. I live in {city}.')
    
showData('Waseem','Solapur')
showData('Alex')

showData(city='Mumbai',name='Alice')

print("-----------------------------")

def showInfo(*info):
    print(info)
    print(info[0],info[1],info[2])
    
showInfo('Variables','Datatypes','Functions')
print("-----------------------------")

def printData(**data):
    print(data)
    print(data['name'], data['city'], data['qual'])

printData(name='Alexa',city='San Fransisco',qual='PHD in Computer Science')
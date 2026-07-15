class Animal:
    __name = ''
    __type = ''
    
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    
    def setType(self,_type):
        self.__type = _type
    def getType(self):
        return self.__type
    
a = Animal()
a.setName('Lion')
a.setType('Wild')
print(f'NAME - {a.getName()}')
print(f'TYPE - {a.getType()}')

a = Animal()
a.setName('Horse')
a.setType('Domestic')
print(f'NAME - {a.getName()}')
print(f'TYPE - {a.getType()}')
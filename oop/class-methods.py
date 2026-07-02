class Person:
    name = 'Sam'
    city = 'California'
    age = 25
    
    def setData(self):
        self.name = input('ENTER NAME OF PERSON - ')
        self.city = input('ENTER CITY OF PERSON - ')
        self.age = input('ENTER AGE OF PERSON  - ')
        print('--------------------------------')
        
    def getData(self):
        print(f'NAME - {self.name}')
        print(f'CITY - {self.city}')
        print(f'AGE  - {self.age}')
        print('__________________________________')
        
p1 = Person()
p2 = Person()
p3 = Person()

p1.setData()
p2.setData()

p1.getData()
p2.getData()
p3.getData()
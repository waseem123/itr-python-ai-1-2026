class Watch:
    def setData(self,watchtype,watchbrand):
        self.watchtype = watchtype
        self.watchbrand = watchbrand
        
    def getData(self):
        print(f'WATCH TYPE  - {self.watchtype}')
        print(f'WATCH BRAND - {self.watchbrand}')
        
class AndroidOS:
    def setData(self):
        self.version = '17.0'
        self.features = ['CALLING','NOTIFICATIONS','LOCATION','MUSIC','HEALTH AND FITNESS']
    
    def getData(self):
        print(f'ANDROID VERSION - {self.version}')
        print('FEATURES - ')
        for i in range(len(self.features)):
            print(f'{i+1}. {self.features[i]}')
            
class SmartWatch(AndroidOS,Watch):
    def setSmartWatch(self,watchPrice):
        self.watchPrice = watchPrice
        
    def getSmartWatch(self):
        print(f'WATCH PRICE - INR. {self.watchPrice}')
        
sm = SmartWatch()
# sm.setData('Digital','boAt')
sm.setData()
sm.setSmartWatch(6500)

sm.getData()
sm.getData()
sm.getSmartWatch()
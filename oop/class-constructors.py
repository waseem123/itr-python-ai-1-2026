class Pen:
    def __init__(self,brand='Raynolds',ink='Green',price=20):
        print('CONSTRUCTOR EXECUTION STARTED...`')
        self.brand = brand
        self.ink = ink
        self.price = price
        
    def getPen(self):
        print(f'BRAND - {self.brand}')
        print(f'INK   - {self.ink}')
        print(f'PRICE - {self.price}')
        print('------------------------------')
        
p1 = Pen('Cello','Blue',15)
p2 = Pen('Camlin','Black',35)
p3 = Pen('Trimax','Red',50)
p4 = Pen()

p1.getPen()
p2.getPen()
p3.getPen()
p4.getPen()
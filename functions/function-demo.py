def getArea():
    r = 10
    area = 3.14 * r ** 2
    print('AREA - ',area)
    
def getSquareArea(side):
    print('AREA OF SQUARE',side**2)
    
def getTriangleArea():
    base = 10
    height = 20
    area = 0.5 * base * height
    return area

def getRectArea(length,breadth):
    return length * breadth

getArea()
getSquareArea(60)
a = getTriangleArea()
print('AREA OF TRIANGLE',a)

rectarea = getRectArea(5,10)
print('AREA OF RECTANGLE',rectarea)

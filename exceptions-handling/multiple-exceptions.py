data = []
try:
    data = ['React','Angular','Node JS','Flask','Spring Boot']
    nr = int(input('ENTER A NUMBER - '))
    dr = int(input('ENTER A NUMBER - '))
    result = nr / dr
    print(result)
    print(data[10])
except ZeroDivisionError:
    print('YOU CAN NOT DIVIDE ANY NUMBER BY ZERO')
except ValueError:
    print('INVALID INPUT')
except:
    print('UNDEFINED ERROR')

finally:
    data.clear()
    print("PROGRAM ENDS HERE")
    
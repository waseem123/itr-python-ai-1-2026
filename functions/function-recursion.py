def showData(count):
    if count>0:
        print('HelloWorld')
        showData(count-1)
    
showData(10)
print('-----------------------')

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))
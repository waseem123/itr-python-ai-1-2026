class AgeError(Exception):
    def __init__(self, message):
        super().__init__(message)
        
        
def checkAge(age):
    if age>=18:
        return True
    else:
        raise AgeError(f'{age} IS NOT A VALID AGE')
    

n = int(input('ENTER THE AGE - '))
print(checkAge(n))
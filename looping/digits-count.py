n = int(input('ENTER A NUMBER - '))
temp = n
count = 0
while(n!=0):
    count+=1
    n //= 10
    
print(f'THERE ARE {count} DIGITS IN {temp}')

n = 178
n = str(n)
print(len(n))
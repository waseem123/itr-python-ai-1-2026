n = int(input('ENTER A NUMBER - ')) #139
temp = n
reverse = 0

while n!=0:
    r = n % 10 # 1
    reverse = reverse * 10 + r  #93 * 10 + 1 =>931
    n //= 10

print(reverse)

if reverse==temp:
    print('PALINDROME')
else:
    print('NOT PALINDROME')
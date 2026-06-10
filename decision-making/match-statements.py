print('1. Biryani - INR. 190')
print('2. Butter Chicken - INR. 450')
print('3. Butter Paneer  - INR. 270')
print('4. Chocolate IceCream - INR. 40')
print('5. Tea - INR. 20')
choice = int(input('ENTER YOUR CHOICE - '))

match choice:
    case 1:
        quantity = int(input('ENTER THE QUANTITY OF BIRYANI - '))
        bill = quantity * 190
        print(f'YOUR BILL FOR {quantity} BIRYANI(s) IS INR. {bill}')
    case 2:
        quantity = int(input('ENTER THE QUANTITY OF BUTTER CHICKEN - '))
        bill = quantity * 450
        print(f'YOUR BILL FOR {quantity} BUTTER CHICKEN(s) IS INR. {bill}')
    case 3:
        quantity = int(input('ENTER THE QUANTITY OF BUTTER PANEER - '))
        bill = quantity * 270
        print(f'YOUR BILL FOR {quantity} BUTTER PANEER(s) IS INR. {bill}')
    case 4:
        quantity = int(input('ENTER THE QUANTITY OF CHOCOLATE ICECREAM - '))
        bill = quantity * 40
        print(f'YOUR BILL FOR {quantity} CHOCOLATE ICECREAM(s) IS INR. {bill}')
    case 5:
        quantity = int(input('ENTER THE QUANTITY OF TEA - '))
        bill = quantity * 20
        print(f'YOUR BILL FOR {quantity} TEA(s) IS INR. {bill}')
        
    case _:
        print('WRONG INPUT! PLEASE ENTER YOUR CHOICE BETWEEN 1 TO 5')
    
print('THANKS! VISIT AGAIN.')
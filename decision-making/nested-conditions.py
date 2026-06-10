age = int(input('ENTER YOUR AGE - '))

if age>=18:
    voterid = input("DO YOU HAVE VOTER ID?(Y:YES | N:NO) - ")
    if voterid=='Y' or voterid=='y':
        print('CONGRATULATIONS! YOU CAN VOTE.')
    else:
        print("SORRY! YOU CAN NOT VOTE.")
else:
    print(f'GET LOST! GROW UP AND THEN COME FOR VOTING AFTER {18-age} YEARS.')   
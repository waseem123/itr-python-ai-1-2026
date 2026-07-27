import os
try:
    os.remove('sample.txt')
    print('FILE DELETED SUCCESFULLY')
except FileNotFoundError as e:
    print(e)
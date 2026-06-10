x = 100
y = 25
z = 130

print(x > y and x > z)
print(x > y and x < z)
print(y < x and z > x)

print(x > y or z < x)
print(x > y or z > x)
print(x < y or x > z)

print(not(not(x < 95)))
set_a = {'Pen','Pencil','Scale','Notebook','Eraser'}
set_b = {'Eraser','Sharpner','Notebook','Pen','Pencil'}

set_c = set_a.symmetric_difference(set_b)
print(set_c)

set_d = set_a ^ set_b
print(set_d)

print('------------------')
# set_b.symmetric_difference_update(set_a)
set_a ^= set_b
print(set_a)
print(set_b)
set_a = {'Pen','Pencil','Scale','Notebook','Eraser'}
set_b = {'Eraser','Sharpner','Notebook','Pen','Pencil'}

set_c = set_b.difference(set_a)
print(set_c)

set_d = set_a - set_b
print(set_d)
print('____________________')
# set_b.difference_update(set_a)
set_b -= set_a
print(set_a)
print(set_b)
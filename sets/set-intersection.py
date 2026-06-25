set_a = {'Pen','Pencil','Scale','Notebook','Eraser'}
set_b = {'Eraser','Sharpner','Notebook','Pen','Pencil'}

set_c = set_a.intersection(set_b)
print(set_c)

set_x = set_a & set_b
print(set_x)

# set_b.intersection_update(set_a)
set_b &= set_a
print(set_a)
print(set_b)


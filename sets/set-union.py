set_a = {'Pen','Pencil','Scale','Notebook','Eraser'}
set_b = {'Eraser','Sharpner','Notebook','Pen','Pencil'}

set_c = set_a.union(set_b)
print(set_c)

set_a.update(set_b)
print(set_a)
print(set_b)

d = set_a|set_b
print(d)


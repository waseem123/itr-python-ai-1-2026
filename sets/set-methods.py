set_X = {'Pen','Pencil','Scale','Notebook','Eraser','Sharpner','Book','Calculator','Writting Pad'}
set_a = {'Pen','Pencil','Scale','Notebook','Eraser'}
set_b = {'Eraser','Sharpner','Notebook','Pen','LED','Pencil','USB Pen Drive'}
set_c = {'Marker Pen','LED','White Board'}
print(set_X.issuperset(set_a))
print(set_X.issuperset(set_b))

print(set_a.issubset(set_X))
print(set_b.issubset(set_X))

print(set_a.isdisjoint(set_b))

print(set_c.isdisjoint(set_b))

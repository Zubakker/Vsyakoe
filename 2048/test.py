a = [[1], [2], [3]]
b = []
for el in a:
    b.append(el.copy())
a[0].append('h')
print(b)
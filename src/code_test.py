a = [1,1,1,2,3]
map = {}
for i in a:
    map[i] = map.get(i, 0) + 1
print(map)
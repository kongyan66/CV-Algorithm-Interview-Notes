a = [(1, 2), (2, 1)]
# sorted(a, key=lambda x:x[1])
a.sort(key = lambda x:x[1])
print(a)
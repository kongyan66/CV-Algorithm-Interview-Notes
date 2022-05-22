import copy
old = [1,[1,2,3],3]
new = copy.deepcopy(old)
 
new[0] = 3
new[1][0] =3

print(old)
print(new)
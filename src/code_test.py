from multiprocessing import BoundedSemaphore


n =3
board = [['.'] * n for _ in range(n)]
res = []
for tem in board:
    tem_str = "".join(tem)
    res.append("".join(tem))
print(res)


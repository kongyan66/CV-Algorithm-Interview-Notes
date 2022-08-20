# n * n的网格放了三个坐标点，且已知道与目标点的曼哈顿距离，求可能的目标点，如果多个取排序后最小的那个

# 解法一：暴力法 搜素所有可能的点
n = int(input())
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
s3 = list(map(int, input().split()))
ans = list(map(int, input().split()))
res = []

for i in range(n):
    for j in range(n):
        a1 = abs(i - s1[0]) + abs(j - s1[1])
        a2 = abs(i - s2[0]) + abs(j - s2[1])
        a3 = abs(i - s3[0]) + abs(j - s3[1])

        if a1 == ans[0] and a2 == ans[1] and a3 == ans[2]:
            res.append([i,j])
res.sort()
print(''.join(map(str, res[0])))
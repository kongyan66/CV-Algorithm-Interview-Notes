from collections import defaultdict
# 当前位置出发得到的最大收益
# 1.确定入参与返回值 入参：到达位置 返回值：当前位置的收益
def dfs(x):
    if x == 0:
        return 0
    if x not in vis:
        dic[x] += dfs(x // 2)
        vis.add(x)
    return dic[x]

# 输入处理
n = 4
p = [2, 3, 4, 5]
v = [2, 5, 2, 4]
# hash表记录宝藏位置与价值
dic = defaultdict(int)
for idx, val in zip(p, v):
    dic[idx] += val        # 有可能一个多个宝藏在同一个位置

vis = set() # 记录走过的位置

# 到达不同，各自的最大收益
# 为啥可以共用dic，因为只能走向比自己大的，所以前面的值不受影响
for x in sorted(dic.keys()):
    print(x)
    dfs(x)
    print(dic)

print(max(dic.values()))
# 2022/8/31 2道编程 20道选择 赛码平台

'''
题目：给一个排序好的数组arr1和一个部分打乱排序的数组arr2，问arr2中排序错误的个数
'''
# 思路：直接对arrb编号然后在arra里面求最长上升子序列的长度l
arra = [5, 4, 3, 2, 1]
arrb = [1, 5, 3, 4, 2]  # 排序错误个数为2
idx = {v:i for i, v in enumerate(arrb)}
last = -1
ans = 0

for v in arra:
    if last < idx[v]:
        last = idx[v]
    else:
        ans += 1
print(ans)
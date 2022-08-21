# 题目：小明有两个一摸一样的数列，但不小心落地打散了一部分，现在两数列为A和B，长度为n和m, 现有两种操作：
# 1.替换：将数列某一个数a改为b, 花费时间|a - b|
# 2.删除：删除某一个数a,花费时间|a|
# 问让两数列相同，所需最小时间
n, m = 1, 1
arr1 = [-9821]
arr2 = [7742]


# 解法：典型的编辑距离问题
def solution(n, m, arr1, arr2):
    import numpy as np
    
    # 1.dp[n][m] 表示数组前n-1,m-1段相等所需最少时间
    dp = np.zeros((n+1, m+1))

    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] + abs(arr1[i - 1])

    for j in range(1, m + 1):
        dp[0][j] = dp[0][j- 1] + abs(arr2[j - 1])

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr1[i-1] == arr2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # 删除当前数字
                #dp[i][j] = dp[i-1][j-1] + min(abs(arr1[i-1]) + abs(arr2[j-1]), abs(arr1[i-1] - arr2[j-1]))
                dp[i][j] = min(dp[i-1][j] + abs(arr1[i-1]), dp[i][j-1] + abs(arr2[j-1]), dp[i-1][j-1] + abs(arr1[i-1] - arr2[j-1]))
    return dp[-1][-1]

if __name__ == '__main__':
    # n, m = map(int, input().split(' '))
    # arr1 = list(map(int, input().split(' ')))
    # arr2 = list(map(int, input().split(' ')))
    res = solution(n, m, arr1, arr2)
    print(res)


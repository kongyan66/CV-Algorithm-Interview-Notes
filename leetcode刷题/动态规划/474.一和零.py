# 题目：给一个字符串列表strs，及整数m,n, 请找出并返回strs的最大子集的大小，要求该子集最多有m个0以及n个1

# 思路：自己看真看不出来是背包问题，这题特殊在有两个背包，m装1，n装0, 这就是一个01二维背包问题了
# 物品就是字符串了，要求子集最大，那么价值就是字符串的个数了(这里每个物品价值都为1了），重量就是0或者1的数量

'''
1. dp[i][j] 表示装i个0，j个1, 所得到的的最大价值(子集长度最大)
2. dp[i][j] = max(dp[i][j], dp[i-zeroNum][j-oneNum] + 1)
   这里和dp[j] = max(dp[j], dp[j-weight[i] + value[i]]) 完全一致
3. dp[i][j] = 0
4.遍历顺序，背包都是逆序
'''

# 解: 01背包 最大值问题
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[0][0] = 0    # 可写可不写
        for item in strs:
            zeroNums = item.count('0')   # python序列通用方法count()
            oneNums = item.count('1')
            for i in range(m, zeroNums-1, -1):  # 01背包, 不能取重复，所以倒序
                for j in range(n, oneNums-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeroNums][j -oneNums] + 1)
        return dp[m][n]
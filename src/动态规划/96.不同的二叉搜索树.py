# 题目：给你一个整数n ，求恰由n个节点组成且节点值从1到n互不相同的二叉搜索树有多少种？返回满足题意的二叉搜索树的种数。

# 思路：化几个图，可以得到一个规律：dp[n] = f(1) + f(2) + .... + f(n)，f(n)表示以n为根节点的二叉搜索树个数
# 进一步分解，f(n)又等于左右子树的二叉搜索树的个数的乘积（组合数，所以用乘法），于是推理出dp[n]
# 题解：https://leetcode.cn/problems/unique-binary-search-trees/solution/hua-jie-suan-fa-96-bu-tong-de-er-cha-sou-suo-shu-b/


class Solution:
    def numTrees(self, n: int) -> int:
        '''
        dp五部曲:
        1.状态定义:dp[i]为当有i个节点时,一共可以组成的二叉搜索树数目
        2.状态转移:dp[3]=dp[0]*dp[2]+dp[1]*dp[1]+dp[2]*dp[0]
            可以比喻成前面一项是左子树情况数,后面一项是右子树情况数,相加即可
            即:dp[n]=∑dp[i]*dp[n-i-1],其中i∈[0,n-1]
        3.初始化:dp[0]=1,dp[1]=dp[0]*dp[0]=1
        4.遍历顺序:正序
        5.返回形式:返回dp[n]
        '''
        dp = [0] * (n+1) # 返回结果是dp[n] 所以长度需加一
        dp[0] = 1        # 无意义 但为了保证乘法不为0
        dp[1] = 1
        for i in range(2, n+1): # 求dp[n]
            for j in range(i):  # 求dp[i]
                dp[i] += dp[j]*dp[i-1-j]
        return dp[n]

# 题目：给一个字符串s和一个字符串列表wordDict作为字典，判断是否可以利用字典中的出现的单词拼接出s

# 思路：字符串s就是背包的容量，字符串列表就是物品，且不限制使用，故是一个完全背包问题
# 要求判断是否得到s,故是一个bool问题

'''
1.dp[j]表示是s[:j](字符串的前j段)是否可由worddict表示
2.dp[0] = True 空字符串可以被表示
3. dp[j] = dp[i] and dp[i+1:n+1] in wordDict
4. 
'''
# 代码随想录版  
from xml.etree.ElementTree import TreeBuilder


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)   # +1为了好初始化，dp[0]无意义，长度为了够必须加一
        dp[0] = True  # 无意义，只为了递推公式
        # 遍历背包
        for j in range(1, len(s)+1): 
            # 遍历物品
            for word in wordDict:
                # 只有字符串长度大于单侧长度，才有可能
                if j >= len(word):
                    # 如果dp[j-len(word)]为True, 且s[j-len(word):j]在字典里，那么该段字符串就可以被表示
                    # 为啥用dp[j] 可认为更新dp吧，选用不同的单词去测试
                    dp[j] = dp[j] or (dp[j - len(word)]  and s[j- len(word):j] == word)
        return dp[len(s)]



# letcode版 好理解
# https://leetcode.cn/problems/word-break/solution/dong-tai-gui-hua-ji-yi-hua-hui-su-zhu-xing-jie-shi/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:       
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(n):
            for j in range(i+1,n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j]=True
        return dp[-1]

# 直接回溯法
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict) # 用O(n)的时间转为哈希表，这样查询只需要O(1)
        def dfs(s):
            # s串用完了，说明找到了
            if not s: 
                return True
            for i in range(len(s)):
                # s[:i+1]子串存在，s[i+1:]另一部分子串存在
                if s[:i+1] in wordDict and dfs(s[i+1:]):
                    return True
            return False
        return dfs(s)

        
# 回溯+记忆化递归
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict) # 用O(n)的时间转为哈希表，这样查询只需要O(1)
        method = dict()
        def dfs(s):
            # 如果记忆中存在，就直接返回
            if s in method: 
                return method[s]
            if not s: 
                return True
            for i in range(len(s)):
                if s[:i+1] in wordDict and dfs(s[i+1:]):
                    method[s] = True  # 实时记录
                    return True
            method[s] = False # 回溯
            return False
        return dfs(s)

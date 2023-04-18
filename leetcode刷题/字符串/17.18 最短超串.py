# 题目：假设你有两个数组，一个长一个短，短的元素均不相同。找到长数组中包含短数组所有的元素的最短子数组，其出现顺序无关紧要。

# 思路：与76.最小覆盖子串完全一致

# 解
class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        n, m = len(big), len(small)
        if n < m:
            return []
        counter = collections.Counter(small)
        need = m

        res = []       # 记录目标子串的起始和结尾
        min_len = float('inf')   # 符合题意的最短子串长度【初始化为一个不可能的较大值】
        left = right = 0         # 滑动窗口的左右边界

        for right in range(n):
            # 窗口右边界右移一位
            ch = big[right]           # 窗口新加入的字符
            if ch in counter:       # 新加入的字符位于t中
                if counter[ch] > 0: # 对当前字符ch还有需求
                    need -= 1       # 此时新加入窗口中的ch对need有影响
                counter[ch] -= 1
            
            # 当need=0,窗口左边界持续右移, 寻找下一种可能
            while need == 0:      # 当need=0 当前窗口已经完全覆盖了t
                # 如果出现了更短的子串
                if right - left + 1 < min_len:  
                    min_len = right - left + 1
                    res = [left, right]  

                ch = big[left]
                if ch in counter:
                    if counter[ch] >= 0:
                        need += 1
                    counter[ch] += 1
                left += 1             # 左边界+1
        return res
       
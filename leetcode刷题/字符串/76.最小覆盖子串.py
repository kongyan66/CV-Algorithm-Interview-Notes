# 题目：给你一个字符串s 、一个字符串t 。返回s中涵盖t所有字符的最小子串。如果s中不存在涵盖t所有字符的子串，则返回空字符串 "" 。

# 思路：滑动窗口 维护一个变长的窗口，用dict记录t各个字母出现的次数，然后不断移动窗口右指针，当找到一个覆盖t的子串窗口，就收缩窗口的左指针，直到不再符合

# 解
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        counter = collections.Counter(t)
        need = m

        start, end = 0, -1       # 记录目标子串s[start, end]的起始和结尾
        min_len = float('inf')   # 符合题意的最短子串长度【初始化为一个不可能的较大值】
        left = right = 0         # 滑动窗口的左右边界

        for right in range(n):
            # 窗口右边界右移一位
            ch = s[right]           # 窗口新加入的字符
            if ch in counter:       # 新加入的字符位于t中
                if counter[ch] > 0: # 对当前字符ch还有需求
                    need -= 1       # 此时新加入窗口中的ch对need有影响
                counter[ch] -= 1
            
            # 当need=0,窗口左边界持续右移, 寻找下一种可能
            while need == 0:      # 当need=0 当前窗口已经完全覆盖了t
                # 如果出现了更短的子串
                if right - left + 1 < min_len:  
                    min_len = right - left + 1
                    start, end = left, right

                ch = s[left]
                if ch in counter:
                    if counter[ch] >= 0:
                        need += 1
                    counter[ch] += 1
                left += 1             # 左边界+1
        return s[start:end+1]
                    



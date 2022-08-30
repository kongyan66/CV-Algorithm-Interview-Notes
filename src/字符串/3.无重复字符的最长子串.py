# 题目：给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

# 思路：滑动窗口

# 利用双指针实现虚拟窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        widows = collections.defaultdict(int)  # 用字典保证每一个字符只出现一次
        left, right = 0, 0 
        res = 0
        
        while right < len(s):
            c = s[right]
            right += 1
            widows[c] += 1
            # 判断左窗口是否需要收缩, 如果有字符出现次数大于1就收缩
            while widows[c] > 1:
                d = s[left]
                left += 1
                widows[d] -= 1
            res = max(res, right - left)
        return res

# 利用list维护一个真实窗口 更好理解
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windows = []
        res = 0
        for i in range(len(s)):
            while s[i] in windows:
                windows.pop(0)
            windows.append(s[i])
            res = max(res, len(windows))
        return res

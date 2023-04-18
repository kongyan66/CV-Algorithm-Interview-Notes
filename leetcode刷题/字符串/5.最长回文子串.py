# 题目：给你一个字符串 s，找到 s 中最长的回文子串。

# 思路：找回文串要从中间开始向两边扩散来判断回文串，但也要分奇偶

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            # 奇数情况
            s1 = self.solution(s, i, i)
            # 偶数情况
            s2 = self.solution(s, i, i+1)
            # 取长度最长的
            if len(s1) > len(res):
                res = s1
            if len(s2) > len(res):
                res = s2
        return res


    # 找回文串的关键技巧是传入两个指针 l 和 r 向两边扩散，因为这样实现可以同时处理回文串长度为奇数和偶数的情况。
    def solution(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 上一个符合的状态
        return s[left+1:right]
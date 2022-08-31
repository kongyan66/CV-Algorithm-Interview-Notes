# 题目：给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。

# 思路：滑动窗口 定长窗口 

# 解
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        cnt = collections.Counter(s1)
        need = m
        right = left = 0

        for right in range(n):
            ch = s2[right]
            if ch in cnt:
                if cnt[ch] > 0:  # 大于零，说明需要，才用减一
                    need -= 1
                cnt[ch] -= 1

            while right - left >= m:
                ch = s2[left]
                if ch in cnt:
                    if cnt[ch] >= 0:
                        need += 1
                    cnt[ch] += 1
                left += 1
            if need == 0:
                return True
        return False
                
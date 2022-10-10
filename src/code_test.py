class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        window = dict()
        need = Counter(t)
        valid = 0
        length = float('inf')

        left, right = 0, 0

        for right in range(len(s)):
            c = s[right]
            if need.count(c):
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            
            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left

                d = s[left]
                left += 1
                if need.count(d):
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return length


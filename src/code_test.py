class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        from collections import defaultdict
        window = defaultdict(int)
        need = Counter(t)
        min_len = float('inf')
        left, right = 0, 0
        match = 0

        while right < len(s):
            c = s[right]
            if c in need:
                window[c] += 1
                # 匹配到字符
                if window[c] == need[c]:
                    match += 1
            right += 1

            while match == len(need):
                # 如果出现了更短的子串
                if right - left < min_len:
                    start = left
                    min_len = right - left

                d = s[left]
                if d in need:
                    window[d] -= 1
                    # 说明此时已经不匹配了
                    if window[d] < need[d]:
                        match -= 1
                left += 1
                    
        return '' if min_len == float('inf') else s[start:start + min_len]

if __name__ == "__main__":
    from collections import Counter





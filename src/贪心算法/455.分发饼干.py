# 题目：对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j]

# 思路1：优先考虑大饼干喂胃口大的
# 饼干不动，胃口去匹配
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        start, count = len(s) - 1, 0
        for i in range(len(g) - 1,  -1, -1):
            if start >= 0 and s[start] >= g[i]:
                count += 1
                start -= 1
        return count

# 思路2：优先考虑小饼干喂胃口小的
# 胃口不动，饼干去匹配
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        start, count = 0, 0
        for i in range(len(s)):
            if start < len(g) and s[i] >= g[start]:
                start += 1
                count += 1
        return count
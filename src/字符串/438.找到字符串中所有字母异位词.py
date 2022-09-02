# 题目：给定两个字符串s和p，找到s中所有p的异位词的子串，返回这些子串的起始索引
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

# 思路：滑动窗口 维护一个固定长len(p)的窗口，每次都去与p比较，若包含p的排列就保存窗口左端
# https://leetcode.cn/problems/minimum-window-substring/solution/by-flix-1kac/


# 解
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if m > n:
            return []
        cnt = collections.Counter(p) # 哈希表：记录需要匹配到的各个字符的数目 返回是一个字典类型
        need = m                     # 记录需要匹配到的字符总数【need=0表示匹配到了】
        res = []

        for right in range(n):
            # 窗口右边界
            ch = s[right]
            if ch in cnt:
                if cnt[ch] > 0:  # 新加入的字符位于p中
                    nedd -= 1    # 此时新加入窗口中的字符对need有影响
                cnt[ch] -= 1
            # 窗口左边界
            left = right - m
            if left >= 0:
                ch = s[left]
                if ch in cnt:
                    if cnt[ch] >= 0:   # 刚滑出的字符位于p中
                        need += 1      # 此时滑出窗口的字符对need有影响
                    cnt[ch] += 1

            if need == 0:              # 找到了一个满足题意的窗口，其左端点为right-m+1
                res.append(right - m + 1)
        return res
                    
        

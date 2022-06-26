# 题目：字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
# 返回一个表示每个字符串片段的长度的列表。

# 思路：第一想法可能是回溯，在遍历的过程中相当于是要找每一个字母的边界，如果找到之前遍历过的所有字母的最远边界，
# 说明这个边界就是分割点了。此时前面出现过所有字母，最远也就到这个边界了。

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 先保存所有字母最后出现的最大小标（最后一次出现的下标）
        hash = [0] * 26
        for i in range(len(s)):
            hash[ord(s[i]) - ord('a')] = i
        left = 0
        right = 0
        result = []
    
        for i in range(len(s)):
            # 更新右边界
            right = max(right, hash[ord(s[i]) - ord('a')])
            # 到达右边界后，计算区间长度，更新左边界
            if i == right:
                result.append(right - left + 1)
                left = i + 1
        return result
            
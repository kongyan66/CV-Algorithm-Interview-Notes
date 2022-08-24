# 题目：给你一个字符串数组 words ，请你找出所有在 words 的每个字符串中都出现的共用字符（包括重复字符）

# 思路：用list做哈希表，保存每个字符中字母除出现的频率，取最小值即为共有的字母

# 解法
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        hash = [0] * 26  # 保存每个字母出现的最小频率
        # hash初始化，后面要取最小值，所以部不能都为零
        for i, c in enumerate(words[0]):
            hash[ord(c) - ord('a')] += 1
        # 遍历除第一个以外的字符出现的频率
        for i in range(1, len(words)):
            tem_hash = [0] * 26
            for j in range(len(words[i])):
                tem_hash[ord(words[i][j]) - ord('a')] += 1
            # 更新hash，保证hash里统计26个字符在所有字符串里出现的最小次数
            for k in range(26):
                hash[k] = min(hash[k], tem_hash[k])
                
        # 将hash统计的字符次数，转换成输出
        for i in range(26):
            while hash[i] != 0:
                res.append(chr(i + ord('a')))
                hash[i] -= 1
        return res
        
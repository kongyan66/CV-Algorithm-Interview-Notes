# 题目：给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

# 思路：考察异位词的编码，如何其输出相同

# 解法一：利用排序相同来编码
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            # sorted()为key，原字符串为value
            keys = "".join(sorted(s))  # sorted输出是list
            if keys not in dic:
                dic[keys] = [s]        # value是一个list
            else:
                dic[keys].append(s)
        return list(dic.values())      # 将dict_values转为list

# 简化下
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for s in strs:
            keys = "".join(sorted(s))
            dic[keys].append(s)
        return list(dic.values())

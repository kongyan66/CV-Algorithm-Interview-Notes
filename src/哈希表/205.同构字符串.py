# 题目：给定两个字符串 s 和 t ，判断它们是否是同构的。
# 如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

# 思路：由于字母没说大小写，所以list就不适合做hash了，还是得用map
# 使用两个map 保存 s[i] 到 t[j] 和 t[j] 到 s[i] 的映射关系，如果发现对应不上，立刻返回 false

from collections import defaultdict
from email.policy import default


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = defaultdict(str)
        map_t = defaultdict(str)

        for i in range(len(s)):
            # 先映射关系，只映射一次
            if not map_s[s[i]]:
                map_s[s[i]] = t[i]
            if not map_t[t[i]]:
                map_t[t[i]] = s[i]
            # 后面就用映射关系去比较
            if map_s[s[i]] != t[i] or map_t[t[i]] != s[i]:
                return False
        return True


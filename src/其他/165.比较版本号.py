# 题目：给你两个版本号 version1 和 version2 ，请你比较它们。

# 解
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for v1, v2 in zip_longest(version1.split('.'), version2.split('.'), fillvalue= '0'):
            a, b = int(v1), int(v2)  # ‘01’ 变 1
            # 如果某一位不相等，则必然不相等，就有大小区别
            if a != b:
                return 1 if a > b else -1
        # 说明两个数相等，则返回零
        return 0
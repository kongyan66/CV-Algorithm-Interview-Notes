# 题目：两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。

# 思路：位运算最方便

# 解法一：计数列表中1的个数
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x ^= y
        return sum(list(map(int, list(bin(x))[2:])))

# 解法二：自己计数字符串中'1'的个数
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x ^= y
        return bin(x).count('1')
        
# 解法三：采用移位来计数
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x ^= y
        count = 0
        while x:
            # 在最低位进行计数
            count += x & 1
            x = x >> 1
        return count
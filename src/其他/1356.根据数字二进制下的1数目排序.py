# 题目：给你一个整数数组 arr 。请你将数组中的元素按照其二进制表示中数字 1 的数目升序排序

# 解法一：
class Solution:
    def countBit(self, n):
        count = 0
        while n:
            n &= n-1 # 没有1了n就为0
            count +=1
        return count
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr = sorted(arr, key=lambda x:(self.countBit(x), x))
        return arr

# 解法二
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr = sorted(arr, key=lambda x:(bin(x).count('1'), x))
        return arr

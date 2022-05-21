# 题目：将输入的字符串反转过来， 不要给另外的数组分配额外的空间

# 思路：双指针 首尾指针
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
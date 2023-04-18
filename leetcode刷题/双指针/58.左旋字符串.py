# 题目：比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

# 解法1.最简单就是直接切片再拼接

# 解法2.先反转区间为前n的子串  再反转区间为n到末尾的子串  后反转整个字符串
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s = list(s)
        s[:n] = self.reverse(s[:n])
        s[n:] = self.reverse(s[n:])
        s = self.reverse(s)
        return "".join(s)

    def reverse(self, res):
       
        left = 0
        right = len(res) - 1

        while left <right:
            res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1
        return res
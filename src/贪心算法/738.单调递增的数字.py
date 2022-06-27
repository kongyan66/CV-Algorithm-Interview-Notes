# 题目：给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。
# 思路：局部最优：遇到strNum[i - 1] > strNum[i]的情况，让strNum[i - 1]--，然后strNum[i]给为9，可以保证这两位变成最大单调递增整数。
# 那么究竟左遍历还是右遍历呢?先试试

# 左遍历：未完全通过
# 数字：332，从前向后遍历的话，那么就把变成了329，此时2又小于了第一位的3了，真正的结果应该是299。
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        n = list(str(n))
        for i in range(1, len(n)):
            if n[i-1] > n[i]:
                n[i-1] = str(int(n[i-1]) - 1)
                n[i:] = '9' * (len(n) - i)
        return int(''.join(n))

# 右遍历
# 那么从后向前遍历，就可以重复利用上次比较得出的结果了，从后向前遍历332的数值变化为：332 -> 329 -> 299
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        n = list(str(n))
        flag = 0
        for i in range(len(n)-1, 0, -1):
            if n[i] < n[i-1]:
                n[i-1] = str(int(n[i-1]) - 1)
                n[i:] = '9' * (len(n) - i)     
        return int(''.join(n))
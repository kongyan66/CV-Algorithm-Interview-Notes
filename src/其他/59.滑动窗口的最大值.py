# 题目：给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

# 思路：如果暴击解法遍历每一个窗口，然后取最大值，时间复杂度为O(nxk),如果k比较大复杂度会很高，故求窗口内最大值可以优化
# 这里我们用单调递减队列来优化，这里需要注意两点
# 1.维持队列单调性 2.维持栈内元素在窗口内

# 解法一：暴力法  O(n*k)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        res = []
        for i in range(0, len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res

   
# 解法二：单调队列 O(n)
# 题解：https://leetcode.cn/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/solution/dong-hua-yan-shi-dan-diao-dui-lie-jian-z-unpy/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = []
        res = []
        for right in range(0, len(nums)):
            # 维持队列单调性
            while deque and nums[right] >= nums[deque[-1]]:
                deque.pop()
            deque.append(right)   # 存元素下标更方便操作
            # 左窗口索引
            left = right - k + 1
            # 如果对列内元素非当前窗口内的，弹出
            while deque and  deque[0] < left:
                deque.pop(0)
            # 窗口形成后才能添加最大值
            if right + 1 >= k:
                res.append(nums[deque[0]]) 
        return(res)
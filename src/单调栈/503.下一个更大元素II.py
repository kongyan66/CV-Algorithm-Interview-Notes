# 题目：给定一个循环数组 nums （ nums[nums.length - 1] 的下一个元素是 nums[0] ），返回 nums 中每个元素的 下一个更大元素 。

# 思路：与496区别是加了循环数组，我们可以将原数组复制一份，这样就变成循环数组了，最后在resize下结果，为了节省空间，我们可以在数组上遍历两次
# 效果是一样的

# 解
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums) * 2
        stack = [0]
        for i in range(1, 2 * len(nums)):
            i = i % len(nums)   # 熟悉的操作呀，可以重复训练数据集n次
            while stack and nums[stack[-1]] < nums[i]:
                res[stack[-1]] = nums[i]
                stack.pop()
            stack.append(i)
        return res[:len(nums)]
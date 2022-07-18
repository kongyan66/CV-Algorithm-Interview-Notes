# 题目：nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。
# 思路：和739类似，前者保存的是索引，本题保存的是元素值，
# 我们先去遍历nums，如果找到异常值，再去nums1匹配，如果存在就保存结果


# 标准写法
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1]*len(nums1)
        stack = [0]
        for i in range(1,len(nums2)):
            # 情况一情况二
            if nums2[i]<=nums2[stack[-1]]:
                stack.append(i)
            # 情况三
            else:
                while len(stack)!=0 and nums2[i]>nums2[stack[-1]]:
                    if nums2[stack[-1]] in nums1:
                        index = nums1.index(nums2[stack[-1]])
                        result[index]=nums2[i]
                    stack.pop()                 
                stack.append(i)
        return result
# 压缩下
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        stack = [0]

        for i in range(1, len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                # 如果nNum是匹配成
                if nums2[stack[-1]] in nums1:
                    index = nums1.index(nums2[stack[-1]]) # 转换到nums1中的索引
                    res[index] = nums2[i]
                stack.pop()
            stack.append(i)
        return res
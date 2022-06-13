# 题目：给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:
# 创建一个根节点，其值为 nums 中的最大值。
# 递归地在最大值 左边 的 子数组前缀上 构建左子树。
# 递归地在最大值 右边 的 子数组后缀上 构建右子树。

# 思路：此题也适合递归
# 写法一：这个写法比之前标准写法更简洁，递归大法秒啊
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # 2. 确定终止条件 如果数组为空，说明到最底层了
        if not nums:
            return None
        # 3.单层递归逻辑
        # 获取数组最大值即数组
        max_value = max(nums)
        max_value_index = nums.index(max_value)
        # 构建当前节点
        root = TreeNode(max_value)
        # 构建左右子叶
        root.left = self.constructMaximumBinaryTree(nums[:max_value_index])
        root.right = self.constructMaximumBinaryTree(nums[max_value_index+1:])
        # 1.确定返回值
        return root

# 写法二：比较规矩的写法
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # 1.确定入参(List)和出参(树的头Node)
        return self.traversal(nums)

    def traversal(self, nums):
        # 2.确定终止条件
        if not nums:
            return None
        max_value = max(nums)
        max_value_index = nums.index(max_value)

        root = TreeNode(max_value)
        root.left = self.traversal(nums[:max_value_index])
        root.right = self.traversal(nums[max_value_index+1:])
        
        return root
# re-2
class Solution:
    # 1.确定递归的入参与返回值
    # 返回值：树的根节点
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # 2.确定递归的终止条件
        if not nums:
            return None
        # 3.确定单调递归逻辑
        max_value = max(nums)
        sparator_point = nums.index(max_value)
        node = TreeNode(max_value)
        left_nums = nums[:sparator_point]
        right_nums = nums[sparator_point+1:]

        node.left = self.constructMaximumBinaryTree(left_nums)
        node.right = self.constructMaximumBinaryTree(right_nums)

        return node
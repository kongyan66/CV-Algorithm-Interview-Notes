# 题目：给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
# 思路：与104、105其实一样,还简单不少，重点寻找分割点，当做当前节点，然后递归左右区间
class Solution:
    # 1.确定递归入参与返回值
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 2.确定递归停止条件 只用于刹车，没有逻辑功能
        if not len(nums):
            return 
        # 3.确定单层递归逻辑
        # 找切割点
        sparator_index = len(nums) // 2
        node = TreeNode(nums[sparator_index])
        # 划分左右区间
        left_nums = nums[:sparator_index]
        right_nums = nums[sparator_index+1:]
        # 递归组装所有节点
        node.left = self.sortedArrayToBST(left_nums)
        node.right = self.sortedArrayToBST(right_nums)
        # 返回最终构成树的根节点，这里也反应了递归的‘归’的含义，由里往外
        return node
        
# 题目：给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，
# 请你构造并返回这颗 二叉树 。

# 思想：构建一棵树，第一件事一定是找根节点，然后想办法构造左右子树。

# 解法一：递归
class Solution:
    # 1.确定入参与返回值
    # 返回值：二叉树的根节点
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 2.确定递归停止条件
        # 第一步：排除特殊情况 如果为空，说明树为空
        if not postorder:
            return None
        # 3.确定单层递归逻辑
        # 找出左子叶和右子叶数组
        # 第二步：从postorder末尾获取根节点值
        rootValue = postorder[-1]
        root = TreeNode(rootValue)
        # 第三步： 找切割点 把数组分为左右两块 最重要一步
        sparator_point = inorder.index(rootValue)
        # 第四步:通过rootValue分割inorder
        in_leftnode = inorder[:sparator_point]
        in_rightnode = inorder[sparator_point+1:]
        # 第五步：通过inorder的左右子树的长度来分割postorder
        post_leftnode = postorder[:len(in_leftnode)]
        post_rightnode = postorder[len(in_leftnode):len(postorder)-1]
        # 第六步：使用递归
        root.left = self.buildTree(in_leftnode, post_leftnode)
        root.right = self.buildTree(in_rightnode, post_rightnode)
        return root



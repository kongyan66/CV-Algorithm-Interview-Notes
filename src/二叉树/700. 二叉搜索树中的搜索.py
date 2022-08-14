# 题目：你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 null 。
# 知识点：
'''
二叉搜索树是一个有序树：
若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
它的左、右子树也分别为二叉搜索树
'''

# 思路：与深度遍历和广度遍历不同，可别忘了二叉树的值是有序的。所以可以利用这一点，每个节点做一次判断
# 就知道往哪边走了

# 解法一：迭代法
class Solution1:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
            else:
                return root

# 解法二；递归法
class Solution:
    # 1.确定入参与返回值
    # 返回值:val存在返回root, 不存在返回None
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # 2.确定终止条件：
        if not root:
            return 
        # 3.单层递归逻辑
        if root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return root

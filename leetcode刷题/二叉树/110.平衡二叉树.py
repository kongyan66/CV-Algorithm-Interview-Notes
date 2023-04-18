# 题目：给定一个二叉树，判断它是否是高度平衡的二叉树。一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1 
# 二叉树节点的深度：指从根节点到该节点的最长简单路径边的条数。
# 二叉树节点的高度：指从该节点到叶子节点的最长简单路径边的条数。本质上就是参考系不一样

# 思路：遍历所有节点,比较左右子节点高度差
# 解法一：迭代法 前序遍历+层序遍历
class Solution1:
    # 用前序遍历去遍历所有节点，然后比较每个节点左右子树的高度差
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [root]
        while stack:
            cur = stack.pop()
            left_height = self.get_height(cur.left)
            right_height = self.get_height(cur.right)
            if abs(left_height - right_height) > 1:
                return False

            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

        return True
    # 用层序遍历获得节点的高度
    def get_height(self, node):
        height = 0
        if not node:
            return height
        que = [node]
        while que:
            for _ in range(len(que)):
                cur = que.pop(0)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            height += 1
        return height

# 递归法
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
       # 1.确定入参和出参
       if self.getheight(root) == -1:
           return False
       else :
           return True
    # 计算节点深度
    def getheight(self, root):
        # 2.确定终止条件
        if root is None:
            return 0
        # 3.确定单层递归逻辑
        # 前序遍历找所有节点
        left_height = self.getheight(root.left)
        right_height = self.getheight(root.right)
        # 后续遍历比较高度差
        if left_height == -1 or right_height == -1: 
            return -1
        # 如果高度差大于一，则记当前节点高度为-1
        if abs(left_height - right_height) > 1:
            return -1
        # 符合要求，就返回当前节点的高度
        else:
            return 1 + max(left_height, right_height)

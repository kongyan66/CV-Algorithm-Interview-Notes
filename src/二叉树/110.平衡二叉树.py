# 题目：给定一个二叉树，判断它是否是高度平衡的二叉树。一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1 
# 二叉树节点的深度：指从根节点到该节点的最长简单路径边的条数。
# 二叉树节点的高度：指从该节点到叶子节点的最长简单路径边的条数。本质上就是参考系不一样

# 思路：遍历所有节点的左右子节点高度，比较高度差

# 解法一：层序遍历
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        que = [root]
        while que:
            cur = que.pop(0)
            if abs(self.getdepth(cur.right) - self.getdepth(cur.left)) > 1:
                return False

            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)        
        return True
    def getdepth(self, node):
        if node is None:
            return 0
        que = [node]
        count = 0
        while que:
            for _ in range(len(que)):
                cur = que.pop(0)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            count += 1
        return count

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
        left_height = self.getheight(root.left)
        right_height = self.getheight(root.right)
        if left_height == -1 or right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        else:
            return 1 + max(left_height, right_height)

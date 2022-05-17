# 题目：给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
# 完全二叉树：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。
# 思路；遍历是比较简单，用一个计数器计数

# 解法一：层序遍历（最简单，但耗时）
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0 
        que = [root]
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

# 解法二：递归法（终于第一次自己写出了递归了，值得庆祝）
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0 
        # 1.确定入参和出参
        return self.getcount(root)

    def getcount(self, node):
        # 2.确定终止条件
        if node is None:
            return 0
        # 3.确定单层逻辑
        left_count = self.getcount(node.left)
        right_count = self.getcount(node.right)
        return left_count+right_count+1

# 解法三：利用二叉树的性质，也用了递归，麻烦点（暂时不看）

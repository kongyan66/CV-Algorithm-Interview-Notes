# 题目：给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
# 思路:之前理解错了，以为最底层最左边节点一定是左子树，其实就是该层的最右边节点，纠结好久
# 所以只要要层序遍历，每次保存该层最左边一个节点即可。

# 解法一：迭代法：层序遍历（比较推荐）
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root != None:
            que = [root]
        result = 0
        
        while que:
            for i in range(len(que)):
                if i == 0:                 # 取每一层最左侧节点的值
                    result = que[i].val
                cur = que.pop(0)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return result
# re-2
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        que = [root]
        while que:
            res = []
            for i in range(len(que)):
                cur = que.pop(0)
                res.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return res[0]
    
# 解法二：递归法（比较难理解）
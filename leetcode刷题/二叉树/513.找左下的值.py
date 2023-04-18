# 题目：给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
# 思路:之前理解错了，以为最底层最左边节点一定是左子树，其实就是该层的最右边节点，纠结好久
# 所以只要要层序遍历，每次保存该层最左边一个节点即可。

# 解法一：迭代法：层序遍历（比较推荐）
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        que = [root]
        result = 0
        while que:
            result = que[0].val
            for _ in range(len(que)):
                cur = que.pop(0)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return result

# 解法二：递归法（比较难理解）
# 找最大深度最左节点的 最大深度最左节点的
class Solution:
    # 定义两个全局变量用于实时保存深度和最左侧的节点值
    # 这里也是一个坑，必须用全局变量，否侧返回值不会被更新
    def __init__(self):
        self.maxleftvalue = 0
        self.maxdepth = -float("INF")
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.recursion(root, 0)
        return self.maxleftvalue
    # 1.确定入参与返回值
    # 入参：curdepth 记录当前深度
    # 返回值：无
    def recursion(self, node, curdepth):
        # 2.确定停止条件
        # 这里比较巧妙，之前一直疑惑为啥他为啥能最左侧节点的值的
        # 首先我们通过前序遍历找到最深的子叶，在左侧节点更新了一下最大值，同一层即使还有别的节点，也不在更新了，这样就找到了
        if not node.left and not node.right:
            if curdepth > self.maxdepth:
                self.maxdepth = curdepth
                self.maxleftvalue = node.val
        # 3.确定单层递归逻辑
        # 其实就是前序遍历逻辑，和求数的最大深度类似，特殊之处在于用了回溯
        if node.left:
            curdepth += 1
            self.recursion(node.left, curdepth) 
            curdepth -= 1  # 回溯  退到父级节点，所以深度减一

        if node.right:
            curdepth += 1
            self.recursion(node.right, curdepth)
            curdepth -= 1  # 回溯
# re_2 
# 到最大深度时第一次遇到的节点就是左下角的节点 这句话很重要
class Solution:
    def __init__(self):
        self.res = 0
        self.max_depth = 0
        self.depth = 0
   
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.DFS(root)
        return self.res

    def DFS(self, root):
        if not root:
            return 
        # 前序遍历位置
        self.depth += 1
        # 到最大深度时第一次遇到的节点就是左下角的节点
        if self.depth > self.max_depth:
            self.max_depth = self.depth
            self.res = root.val
        
        self.DFS(root.left)
        self.DFS(root.right)
        # 后续遍历位置
        self.depth -= 1  # 回溯 注意两次递归也只写一个
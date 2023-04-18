# 题目：给定二叉搜索树（BST）的根节点 root 和要插入树中的值 value ，将值插入二叉搜索树
# 思路：根据二叉搜索树的有序性，只要找到他的父节点（值大于它）接入即可

# 解法一：迭代法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        parent = None
        cur = root
        # 定位要插入位置父节点的位置
        while cur: 
            if cur.val > val:
                parent = cur
                cur = cur.left
            elif cur.val < val:
                parent = cur
                cur = cur.right
            
        if parent.val > val:
           parent.left = TreeNode(val)
        else:
           parent.right = TreeNode(val)
        return root

# 解法二： 递归法 有返回值 
# 不太好理解 这个root是怎么到达空节点
class Solution:
    # 1.确定入参与出参
    # 返回值是当前路径节点
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 2.确定终止条件 
        # 找到遍历节点为None的时候，就是要插入节点的位置，返回要插入的节点
        if not root:
            return TreeNode(val)
        # 3.单层递归逻辑
        # 从上到下不断比较当前节点与val的值，决定放左边还是右边
        # 直到root.left 为空时，我们就把两个节点接上
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        # 同理
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        # 返回最终更新后树的根节点 疑问：这个root一直在变，最后怎么又变成根节点了呢？因为回溯
        return root 

# 解法三：递归法 无返回值  比较好理解， 和迭代法思路基本一致
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        parent = None
        if not root:
            return TreeNode(val)
        # 1.确定入参与返回值 无返回值
        def recursion(cur, val):
            nonlocal parent
            # 2.确定递归停止条件 当到达子叶时，决定val节点放哪边
            if not cur:
                if parent.val > val:
                    parent.left = TreeNode(val)
                elif parent.val < val:
                    parent.right = TreeNode(val)
                return 
            
            # 3.单层递归逻辑
            parent = cur
            if cur.val > val:
                recursion(cur.left, val)
            elif cur.val < val:
                recursion(cur.right, val)
          
        recursion(root, val)
        return root

# 解法四：最简单的
# 题中说了，给的值与树中的值都不同，所以肯定是在树的最下边嘛，我们找到符合二叉搜索树大小关系的空节点位置，插入即可，没有破坏原结构
# 前面的方法动树的结构就太麻烦了
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        # 有返回值 子树的根节点
        def recursion(root, val):
            if not root:
                return TreeNode(val)
            # 加了if判断, 说明只搜索一边
            if root.val > val:
                root.left = recursion(root.left, val) # 后续遍历
            if root.val < val:
                root.right = recursion(root.right, val)
            return root

        recursion(root, val)
        return root
        
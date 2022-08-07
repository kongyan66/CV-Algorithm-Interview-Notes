# 题目：给你二叉树的根结点 root ，请你将它展开为一个单链表：

# 解法一：先前序遍历，列表保存节点，后在按顺序拼接
class Solution:
    def __init__(self):
        self.list_node = []
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.recursion(root)
        for i in range(len(self.list_node) - 1):
            self.list_node[i].left = None
            self.list_node[i].right = self.list_node[i+1]

    def recursion(self, node):
        if not node:
            return 
        self.list_node.append(node)
        self.recursion(node.left)
        self.recursion(node.right)

# 解法二：边遍历，边组装  
# 此题不能用前序遍历，因为组装会破坏原有结构，导致遍历顺序出错。用后续遍历就不会有这个问题了
# 以下这个写法实在理解不了
class Solution:
    def __init__(self):
        self.pre = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.recursion(root)

    def recursion(self, node):
        if not node:
            return 
        self.recursion(node.right)
        self.recursion(node.left)
        # 后续操作
        node.left = None
        node.right = self.pre
        self.pre = node

# 换一个写法就好理解多了
class Solution:
    def __init__(self):
        self.pre = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.recursion(root)

    def recursion(self, node):
        if not node:
            return 
        # 1、左右子树已经被拉平成一条链表
        self.recursion(node.left)
        self.recursion(node.right)

        left = node.left
        right = node.right 
        #  2、将左子树作为右子树
        node.left = None
        node.right = left
        # 3、将原先的右子树接到当前右子树的末端
        tem = node
        while tem.right:
            tem = tem.right
        tem.right = right
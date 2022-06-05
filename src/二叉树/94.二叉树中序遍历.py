# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = rightS
# 图解见 基础知识.md
# 因为要访问的元素和要处理的元素顺序是不一致的，所以写法和前序遍历有区别
# 解法一：迭代法 标准写法
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        cur = root
        while stack or cur:
            # 利用cur去获得节点路径（定位）
            # cur 不为空就添加最右侧节点，直到最底层
            if cur:
                stack.append(cur)
                cur = cur.left
            # 处理节点值（存值）
            else:
                # 保存节点值
                node = stack.pop()
                res.append(node.val)
                # cur指向右节点，这点很重要
                cur = node.right
        return res

      
# 统一写法：标记法
# 要处理的节点放入栈之后，紧接着放入一个空指针作为标记
# 简单记： 中序遍历：左中右 -> 入栈顺序：右中左
class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        if root is not None:
            stack.append(root)
      
        while stack:
            node = stack.pop()       # 将该节点弹出，避免重复操作，下面再将右中左节点添加到栈中
            # 入栈顺序：右中左 这样出栈顺序刚好对应过来
            if node is not None:
                if node.right:       # 添加右节点（空节点不入栈）
                    stack.append(node.right)
                # 关键之处：中节点需要做标记，其他遍历顺序也是这做
                stack.append(node)   # 添加中节点
                stack.append(None)   # 空节点入栈，作为标记，表明该节点还未处理
                if node.left:
                    stack.append(node.left)   # 添加左节点
            else:                    #  只有遇到空节点的时候，才将下一个节点放进结果集
                node = stack.pop()   #  重新取出栈中元素
                result.append(node.val)
        return result

# 解法三： 递归法 和前序遍历，后序遍历写法统一

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.recursion(root, res)
        return res

    def recursion(self, node, res):
        if node is None:
            return 
        self.recursion(node.left, res)
        res.append(node.val)
        self.recursion(node.right, res)
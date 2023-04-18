# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
# 遍历问题：递归或迭代

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 递归遍历
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 局部变量存放节点值
        res = []
        self.recursion(root, res)
        return res

    # 因为入参与上面函数不一致，所以只能分开写，后面会遇到很多合一起的
    # 1.确定入参与返回值
    # 入参就是欲处理的节点了（只去考虑一个节点，递归一次我们只处理一个节点）
    # 无返回值，因为我们需要的节点的值保存在一个单独的列表（局部变量）中，所以不需要返回任何值
    def recursion(self, node, res):
        # 2.确定终止条件
        # 因为无有效返回值，所以为了让递归停下来，我们返回一个空值。
        # 一方面保证递归及时停下来，这样后面的逻辑才不会报错；另一方面防止爆栈
        if node is None:
            return 
        # 3.确定单层递归逻辑
        # 前序遍历是中左右的循序，所以在单层递归的逻辑，是要先取中节点的数值，然后是左右
        res.append(node.val)
        self.recursion(node.left, res)
        self.recursion(node.right, res)

# 小结
# 前序遍历：中左右  后序遍历：左右中 中序遍历：左中右

# 迭代遍历 注意顺序 空节点不如栈
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      if root is None:
        return []

      result = []
      stack = [root]
      while stack:
        node = stack.pop()  
        # 先处理中间节点
        result.append(node.val)
        # 再处理右边节点
        if node.right: # 空节点不入栈
          stack.append(node.right)
        # 最后处理左边节点
        if node.left:
          stack.append(node.left)
      return result

# 统一写法：标记法
# 要处理的节点放入栈之后，紧接着放入一个空指针作为标记
# 简单记： 前序遍历：中左右 -> 入栈顺序：右左中
class Solution3:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        if root is not None:
            stack.append(root)
      
        while stack:
            node = stack.pop()       # 将该节点弹出，避免重复操作，下面再将右中左节点添加到栈中
            # 节点按顺序入栈：右中左 这样出栈顺序刚好对应过来
            if node is not None:
                # 关键之处：中节点需要做标记，其他遍历顺序也是这做
                stack.append(node)   # 添加中节点
                stack.append(None)   # 空节点入栈，作为标记，表明该节点还未处理
                if node.left:
                    stack.append(node.left)   # 添加左节点（空节点不入栈）
                if node.right:       # 添加右节点（空节点不入栈）
                    stack.append(node.right)

           # 把栈中节点值拿出来
            else:                    #  只有遇到空节点的时候，才将下一个节点放进结果集
                node = stack.pop()   #  重新取出栈中元素
                result.append(node.val)
        return result
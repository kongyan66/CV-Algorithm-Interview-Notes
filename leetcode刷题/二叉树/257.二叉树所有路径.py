# 题目：给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
# 思路：用前序遍历去走一遍(中左右），同时每走一步更新路径

# 解法一:迭代法
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        stack = [root]             # 保存节点的栈:stack
        path_st = [str(root.val)]  # 保存路径的栈:stack（实时更新）
        result = []                # 保存最终结果：list
        while stack:
            cur = stack.pop()
            path = path_st.pop()
            # 如果当前节点为叶子节点，添加路径到结果中（说明到底了）
            if not (cur.left or cur.right):
                result.append(path)
            if cur.right:
                stack.append(cur.right)
                path_st.append(str(path)+'->'+str(cur.right.val))  
            if cur.left:
                stack.append(cur.left)
                path_st.append(str(path)+'->'+ str(cur.left.val))
        return result

# 解法一:递归法
# 这里首次自己写了回溯，用于path的更新，避免重复（其实有递归必然有回溯，归嘛，只是这一步由系统自送完成，我们看不到而已）
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        result = []
        if not root:
            return result
        self.recursion(root, path, result)
        return result
    # 1.确定递归的返回值与参数
    def recursion(self, node, path, result):
        # 因为终止条件时叶子节点，如果放在下面，递归就结束了，叶子节点的值还未来及保存
        path.append(node.val)
   
        # 2.确定终止条件
        if not node.left and not node.right:
            # 处理中节点（前序遍历）,为了方便回溯（使用pop）,我们用list来保存路径，但->需要单独处理
            tem = ''
            for i in range(len(path)):
                tem += str(path[i]) + '->'
            result.append(tem[:-2])    # 最后一个->多余了
            return 
        # 3.单程递归逻辑
        
        if node.left:
            # 递归与回溯一一对应
            self.recursion(node.left, path, result) # 递归
            path.pop() # 回溯
        if node.right:
            self.recursion(node.right, path, result) # 递归
            path.pop() # 回溯


# re-3
class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.recursion(root)
        return self.res
    # 1.确定入参与返回值
    # 无返回值 有人工回溯
    def recursion(self, root):
        self.path.append(root.val)
        if not root.left and not root.right:
            tem = ''
            for item in self.path:
                tem += str(item) + '->'
            self.res.append(tem[:-2])
            return 
        if root.left:
            self.recursion(root.left)
            self.path.pop()
        if root.right:
            self.recursion(root.right)
            self.path.pop()
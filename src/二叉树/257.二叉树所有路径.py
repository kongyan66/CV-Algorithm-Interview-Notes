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
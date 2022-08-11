# 题目：给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
# 思路：通过DFS进行搜索路径，然后用一个栈记录路径，用回溯去维护路径的唯一性

# 递归法：
# 此题若是拆开，就得这么定义了：def recursion(node, result, path, targetsum)，不然变量找不到结果就会异常
# 所以还是写到一起吧
class Solution:
    # 1.确定入参与返回值
    # 无返回值
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        if not root:
            return result
        path = [root.val]
        def recursion(node):
            # 2.确定递归停止条件
            # 两种情况：1.一是到达子叶节点未找到合适路径  2.到达叶子节点且找到合适路径
            if not node.left and not node.right:
                if sum(path) == targetSum:
                    result.append(path.copy())
                return 
            # 3.确定单层递归逻辑
            # DFS搜索过程
            if node.left:
                path.append(node.left.val)
                recursion(node.left)
                path.pop()
            if node.right:
                path.append(node.right.val)
                recursion(node.right)
                path.pop()
        recursion(root)
        return result   
        
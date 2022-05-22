# 题目：判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。
# 如果存在，返回 true ；否则，返回 false 。

# 思路：前序遍历每一个路径的节点，同时记录该结点所在路径值之和

# 解法一：迭代法 前序遍历
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        que = [(root, root.val)]    # 节点及对所在路径值之和
        while que:
            cur, cur_sum = que.pop(0)
            if cur.right:
                que.append((cur.right,cur_sum+cur.right.val))
            if cur.left:
                que.append((cur.left, cur_sum+cur.left.val))
            # 没有左右子叶，说明到最低端了，就是一条完整路径了
            if cur.left == None and cur.right == None and cur_sum == targetSum:
                return True
        return False




# 解法二：迭代法 改自257.二叉树所有路径 
# 抱着不作死就不会死的心态，也可以同步保存每个节点的路径，当到达最低层节点是对路径求和，然后与目标值比较
# 本质思路和解法一完全一致，这里也有一个坑：python的赋值是引用而不是重新开辟空间，所以直接修改会导致原来的值也变化
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        que = [(root, [root.val])]

        while que:
            cur, path = que.pop(0)
            if cur.left:
                path_left = path.copy()
                path_left.append(cur.left.val)
                que.append((cur.left, path_left))
            if cur.right:
                path_right = path.copy()
                path_right.append(cur.right.val)
                que.append((cur.right, path_right))
            if cur.left == None and cur.right == None and sum(path) == targetSum:
                return True  
        return False


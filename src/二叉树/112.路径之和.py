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
# re-2
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        st = [(root, [root.val])]
        while st:
            cur, path = st.pop()
            # 前序遍历
            if cur.right:
                # 这里必须对path.copy()赋值指向一个新变量，不能直接进行append()操作
                path_right = path.copy()
                path_right.append(cur.right.val)
                st.append((cur.right, path_right))
            if cur.left:
                path_left = path.copy()
                path_left.append(cur.left.val)
                st.append((cur.left, path_left))
            # 判断是否满足条件
            if not cur.left and  not cur.right:
                if sum(path) == targetSum:
                    return True
        return False

# 解法二： 递归法
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.recursion(root, targetSum - root.val)

    # 1.确定入参与返回值
    # 入参：node, targetsum 返回值：根节点到子叶节点是否存在和为target的路径
    def recursion(self, node, sum):
        # 2.确定终止条件
        # 当到达子叶节点且路径和==target时，返回True
        if not node.left and not node.right and sum == 0:
            return True
        # 3.确定递归逻辑 
        # 其实还是DFS，顺序这并不重要
        if node.left:
            sum -= node.left.val
            if self.recursion(node.left, sum):
                return True
            sum += node.left.val  # 回溯
        if node.right:
            sum -= node.right.val
            if self.recursion(node.right, sum):
                return True
            sum += node.right.val # 回溯
        return False
# re-2 改112.路径之和
class Solution:
    def __init__(self):
        self.path = []
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.recursion(root, targetSum)
         
    def recursion(self, node, targetSum):
        self.path.append(node.val)
        if not node.left and not node.right:
            if sum(self.path) == targetSum:
                return True 
            else:
                return False
        if node.left:
            if self.recursion(node.left, targetSum):
                return True
            self.path.pop()
        if node.right:
            if self.recursion(node.right, targetSum):
                return True
            self.path.pop()
        return False
# re-3 隐藏回溯
    def recursion(self, node, targetSum):
        if not node:
            return False
        # 到达叶子节点就判断
        if not node.left and not node.right and targetSum - node.val == 0:
            return True
        # 这里回溯咋体现的点啊
        return self.recursion(node.left, targetSum - node.val) or self.recursion(node.right, targetSum - node.val)
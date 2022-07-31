# 题目：给定一个二叉树，找出其最小深度。
# 说明：最小深度是从根节点到最近叶子节点的最短路径上的节点数量（叶子节点是指没有子节点的节点）

# 思路：套用层序遍历模板，遇到子叶节点就返回计数器结果
# 解法一：迭代法
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        count = 0
        if not root:
            return count
        que = [root]
        while que:
            count += 1
            for _ in range(len(que)):
                cur = que.pop(0)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                # 遇到无子节点的就返回
                if not cur.left and not cur.right:
                    return count

# 解法二：递归法
# 可见递归法关注的是局部事件，比如此题，我们算好一个节点的深度，递归后就能算出一个树的深度 
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 1.确定入参和出参
        return self.getdepth(root)

    def getdepth(self, node):
        # 2.确定停止条件
        if node is None:
            return 0
        # 3.确定单层递归逻辑
        left_depth = self.getdepth(node.left)
        right_depth = self.getdepth(node.right)
        # z这里容易出错：最小深度是从根节点到最近叶子节点的最短路径上的节点数量，如果左子叶无节点，深度并不一定是1
        # 如果左子叶为空，就看右子叶最小深度
        if node.left and not node.right:
            return left_depth + 1
        # 如果右子叶为空，就看左子叶为空
        elif not node.left and node.right:
            return right_depth + 1
        # 如果左右子节点均存在，看左右子叶的最小深度
        else:
            return min(left_depth, right_depth) + 1
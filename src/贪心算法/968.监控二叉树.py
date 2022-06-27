# 题目：给定一个二叉树，我们在树的节点上安装摄像头。节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
# 计算监控树的所有节点所需的最小摄像头数量。

# 思路：局部最优：让叶子节点的父节点安摄像头，所用摄像头最少，整体最优：全部摄像头数量所用最少！
# 先给叶子节点父节点放个摄像头，然后隔两个节点放一个摄像头，直至到二叉树头结点。
# 每个节点有三种状态：0：该节点无覆盖 1：本节点有摄像头 2:本节点有覆盖

# 写法一：
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        result = 0
        # 4.头结点没有覆盖
        def recursion(root):
            nonlocal result
            # 空节点也要有覆盖
            if not root:
                return 2
            
            left = recursion(root.left)
            right = recursion(root.right)
            # 中间节点，处理逻辑, 有以下四类情况：
            # 1.左右节点均有覆盖, 此时中间节点应该就是无覆盖的状态了

            if left == 2 and right ==2:
                return 0
            # 2.左右节点至少有一个无覆盖的情况, 父节点就应该放摄像头。
                # left == 0 && right == 0 左右节点无覆盖
                # left == 1 && right == 0 左节点有摄像头，右节点无覆盖
                # left == 0 && right == 1 左节点有无覆盖，右节点摄像头
                # left == 0 && right == 2 左节点无覆盖，右节点覆盖
                # left == 2 && right == 0 左节点覆盖，右节点无覆盖
            elif left == 0 or right == 0:
                result += 1
                return 1
            # 3.左右节点至少有一个有摄像头, 那么其父节点就应该是2（覆盖的状态）
            elif left == 1 or right == 1:
                # left == 1 && right == 2 左节点有摄像头，右节点有覆盖
                # left == 2 && right == 1 左节点有覆盖，右节点有摄像头
                # left == 1 && right == 1 左右节点都有摄像头
                return 2
        if recursion(root) == 0:
            result += 1
        return result

# 写法二： 为啥result值不变化，77.组合也是这种写法是可以的呀
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        result = 0
        if self.recursion(root, result) == 0:
            result += 1
        return result
        # 4.头结点没有覆盖
    def recursion(self, root, result):
        # 空节点也要有覆盖
        if not root:
            return 2
        
        left = self.recursion(root.left, result)
        right = self.recursion(root.right, result)
        # 中间节点，处理逻辑, 有以下四类情况：
        # 1.左右节点均有覆盖, 此时中间节点应该就是无覆盖的状态了
        if left == 2 and right ==2:
            return 0
        # 2.左右节点至少有一个无覆盖的情况, 父节点就应该放摄像头。
        elif left == 0 or right == 0:
            result += 1
            return 1
        # 3.左右节点至少有一个有摄像头, 那么其父节点就应该是2（覆盖的状态）
        elif left == 1 or right == 1:
            return 2
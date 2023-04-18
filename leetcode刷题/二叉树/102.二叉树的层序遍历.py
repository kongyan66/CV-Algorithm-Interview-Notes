# 题目：给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
# 考察：队列  队列先进先出，符合一层一层遍历的逻辑，而是用栈先进后出适合模拟深度优先遍历也就是递归的逻辑。
# https://leetcode.cn/problems/binary-tree-level-order-traversal/solution/die-dai-di-gui-duo-tu-yan-shi-102er-cha-shu-de-cen/
# 解法一： 迭代法
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        que = [root]
        results = []
        
        while que:
            res =[]
            # 遍历当前层的宽度
            for _ in range(len(que)): # 循环内只算一次
                # 每次遍历，当前层所有节点均处理完（弹完了）
                cur = que.pop(0)
                res.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(res)
        return results

# 解法二：递归法  这个递归着实不太好理解
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
      res = []
      self.recursion(root, 0, res)        # 头结点的深度为0
      return res 
    # 1.确定入参&返回值
    def recursion(self, node, depth, res):
        # 2.确定终止条件
        if not node:
            return 
        # 3.确定单层递归逻辑
        # 为当前层分配一个空列表
        if len(res) == depth:   # 这个很巧妙啊，res的长度刚好是depth, 省去一个局部变量List存每一层的值
            res.append([])
        # 将当前节点值放入列表
        res[depth].append(node.val)
        # 处理左右子节点
        if node.left:
            self.recursion(node.left, depth+1, res)
        if node.right:
            self.recursion(node.right, depth+1, res)
        

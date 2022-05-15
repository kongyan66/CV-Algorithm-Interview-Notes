# 题目：给你两棵二叉树 root 和 subRoot。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。
# 如果存在，返回 true ；否则，返回 false 。

# 思路：要判断一个树t是不是树s的子树，那么可以判断t是否和树s的任意子树相等。那么就转化成100.相同的树.py 
# 解法：
class Solution1:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and not subRoot:
            return True
        # 前序遍历找所有的节点
        que = [root]
        while que:
            cur = que.pop(0)
            # 与subRoot逐一比较
            if self.compare(cur, subRoot): return True
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
        return False
    # 100.相同的树
    def compare(self, q, p):
        if q != None and p == None: return False
        elif q == None and p != None: return False
        elif q == None and p == None: return True
        elif q.val != p.val: return False

        left = self.compare(q.right, p.right)
        right = self.compare(q.left, p.left)
        return left and right
# 题目：给你一个二叉树的根节点 root ， 检查它是否轴对称。
# 思路：判断左右子树的节点是否相同

# 解法一：遍历法 这里是同时遍历左右子树，和之前遍历左右节点有所区别
class Solution1:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        que = []
        que.append(root.left) # 左子树的头结点
        que.append(root.right) # 右子树的头结点
        while que:
            left_cur = que.pop(0)  # 每次循环比较一对节点
            right_cur = que.pop(0)
            # 如果左右节点都为空就继续比较
            if not left_cur and not right_cur:
                continue
            # 如果只有一个节点为空，或者不为空但值不同
            if not left_cur or not right_cur or left_cur.val != right_cur.val:
                return False
            # 每次循环入四个节点，说明出的比入的慢，慢慢查嘛，总能干完
            que.append(left_cur.left)      # 这里之前有个疑惑：就是这个循环怎么停的，一直append不就一直有吗，其实节点Node为None时，
            que.append(right_cur.right)    # 由于前面的判断条件，append(Node.left)就停止了。
            que.append(left_cur.right)
            que.append(right_cur.left)
        return True

# 解法二：迭代法（还是不熟啊）
# 迭代三要素：
# 1.确定入参与出参：左右子树的节点  返回是否对称：bool
# 2.确定终止条件：节点为空和值不相等
# 3.确定单层递归的逻辑：比较左右子树节点外侧和内侧是否相等

class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # 1.递归的入参与出参
        return self.compare( root.left, root.right)
    def compare(self, left, right):
        # 2.递归停止条件
        # 首先排除空节点的情况
        if left == None and right != None: return False
        elif left != None and right == None: return False
        elif left == None and right == None: return True
        # 再排除值不相等的情况
        # 其他情况就是不为空，且值相等，就可以继续递归了
        elif left.val != right.val: return False
        
        # 3.确定单层递归的逻辑
        # 分别比较外侧和内侧是否相等
        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        return outside and inside

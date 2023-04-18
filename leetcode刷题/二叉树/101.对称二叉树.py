# 题目：给你一个二叉树的根节点 root ， 检查它是否轴对称。
# 思路：判断左右子树的节点是否相同

# 解法一：迭代法 这里是同时遍历左右子树，和之前遍历左右节点有所区别
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

# 解法二：递归法（还是不熟啊）
# 递归三要素：
# 1.确定入参与出参：左右子树的节点  返回是否对称：bool
# 2.确定终止条件：节点为空和值不相等
# 3.确定单层递归的逻辑：比较左右子树节点外侧和内侧是否相等

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # 1.确定入参和返回值
        # 入参就是两个树的根节点了
        # 返回值是判断当前节点是否镜像对称的bool值
        return self.recursion(root.left, root.right)

    def recursion(self, left_node, right_node):
        # 2.确定终止条件
        # 有必然四种情况需要考虑
        # 左右都为空
        if not left_node and not right_node:
            return True
        # 左右有一个为空
        elif not left_node and right_node:
            return False
        elif left_node and  not right_node:
            return False
        # 左右不为空，但值不相等
        # 这里容易疑惑，为啥值相等的不考虑了，值相等就继续向下递归呀，一旦return就终止递归了呀，就没有后续了
        elif left_node.val != right_node.val:
            return False
        # 3.确定单层递归逻辑
        # 说白了就是继续往下比较（这样递归才能传递下去）
        outside = self.recursion(left_node.left, right_node.right)
        inside = self.recursion(left_node.right, right_node.left)
        return outside and inside
    
        # 之前错误写法
        # 说明对递归的返回值没有真正理解，这是两颗逐步变深的树，指导最后回溯告诉你，其左侧与也测是否对称（bool）
        # 只有左右侧都对称，才说明两个树镜像对称
        self.recursion(left_node.left, right_node.right)
        self.recursion(left_node.right, right_node.left)
        return True 
# 题目：合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；
# 否则，不为 null 的节点将直接作为新二叉树的节点。
# 思路：遍历一个树逻辑是一样的，只不过传入两个树的节点，同时操作

# 解法一：递归法
class Solution:
    # 1.确定递归入参与返回值
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # 2.确定递归停止条件(这一步很关键，有点抽象)
        if not root1:
            return root2
        elif not root2:
            return root1
        # 3.单层递归逻辑
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1


# 解法二：迭代法 前序遍历  
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        que =[]
        que.append(root1)
        que.append(root2)

        while que:
            node1 = que.pop(0)
            node2 = que.pop(0)
            # 我们选择node1作为合并的树(这样不用重新开辟空间保存一颗树，节省空间)
            node1.val += node2.val
            if node1.left and node2.left:
                que.append(node1.left)
                que.append(node2.left)
            if node1.right and node2.right:
                que.append(node1.right)
                que.append(node2.right)
            # 考虑node1为空，node2不为空，那就借用node2的子树
            if not node1.left and node2.left:
                node1.left = node2.left
            if not node1.right and node2.right:
                node1.right = node2.right
        return root1
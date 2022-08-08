# 题目：给你二叉树的根节点root ，返回其节点值的锯齿形层序遍历,即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行。
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[20,9],[15,7]]

# 思路：最简单思路是，正常层序遍历，对数组动手脚，另一种思路和S型遍历一致，用双栈来维护遍历顺序

# 解法一：
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        left_stack = []
        right_stack = []
        left_stack.append(root)
        res = []
        if not root:
            return res
        while left_stack or right_stack:
            tem = []
            # 奇数层正序
            while left_stack:
                cur = left_stack.pop()
                tem.append(cur.val)
                if cur.left:
                    right_stack.append(cur.left)
                if cur.right:
                    right_stack.append(cur.right)
            # 防止保存空列表
            if  tem:
                res.append(tem) 
            tem = []
            # 偶数层逆序
            while right_stack:
                cur = right_stack.pop()
                tem.append(cur.val)
                if cur.right:
                    left_stack.append(cur.right)
                if cur.left:
                    left_stack.append(cur.left)
            if  tem:
                res.append(tem)
        return res
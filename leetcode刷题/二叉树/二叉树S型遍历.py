# 题目：层序遍历是一行行的，反S型遍历是按S型遍历节点 （大疆-机器学习工程师-笔试-2022.08.07）

# 思路：使用两个堆栈进行遍历 每一层使用一个栈进行遍历。

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        left_stack = []
        right_stack = []
        left_stack.append(root)
        res = []

        while left_stack or right_stack:
            while left_stack:
                cur = left_stack.pop()
                res.append(cur.val)
                # 如果是正S遍历，这两块反着来就好
                # 偶数层要逆序，应为用栈维护，所以正序放入
                if cur.left:
                    right_stack.append(cur.left)
                if cur.right:
                    right_stack.append(cur.right)
            while right_stack:
                cur = right_stack.pop()
                res.append(cur.val)
                # 奇数层要正序，应为用栈维护，所以逆序序放入
                if cur.right:
                    left_stack.append(cur.right)
                if cur.left:
                    left_stack.append(cur.left)
        return res  
   
                

# 题目：中等 给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
# 思路：还是层序遍历的模板，区别是每一层左边的节点指向它右边的，最后一个不用管，所以这里用列表当队列更方便些（队列不能直接索引取值）

class Solution1:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        que = [root]   # 用列表当队列
        while que:
            size = len(que) 
            for i in range(size):
                cur = que.pop(0)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                if i == size - 1:       # 最后一个节点不管，比如一层有两个节点(n)，只需执行一次（n-1)，但不能放在前面执行，存节点可一个不能少
                    break
                cur.next = que[0]      # 指向它相邻右边的节点
        return root

# review-2
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        que = [root]
        while que:
            width = len(que)
            for i in range(width):
                cur = que.pop(0)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                if i < width-1:
                    cur.next = que[0] 
        return root

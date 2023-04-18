# 题目：给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历），树的序列化输入是用层序遍历，每组子节点都由 null 值分隔
# 说明：这里的N叉树和二叉树节点有些区别（N叉树下面可能有N个节点，而不是二叉树的两个，首先看下定义
#   cur.children 是 Node 对象组成的列表，也可能为 None
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        from collections import deque
        results = []
        if root is None:
            return results
        que = deque([root])
        while que:
           result = []
           for _ in range(len(que)):
               cur = que.popleft()
               result.append(cur.val)
               # 唯一变的地方
               if cur.children:
                   que.extend(cur.children)  # 用extend说明cur.children 是一个列表
           results.append(result)
        return results

# re-2
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        results = []
        if not root:
            return results
        que = [root]
        while que:
            res = []
            for _ in range(len(que)):
                cur = que.pop(0)
                res.append(cur.val)
                if cur.children:
                    que.extend(cur.children)
            results.append(res)
        return results

# 题目：给一个二叉树，填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
# 思路：和116完全一样，这里写法换了下，看起来也优雅些
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = [root]
        while queue:
            size = len(queue)  
            tail = None             # 尾结点标记
            for i in range(size):   
                cur = queue.pop(0)
                if tail:            # 让尾节点指向当前节点
                    tail.next = cur 
                tail = cur          # 当前节点成为尾结点
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right) 
        return root
# review-2
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None 
        que = [root]
        while que:
            size = len(que) 
            for i in range(size):
                cur = que.pop(0)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                # 只需要把同一层节点连起来就行
                if i < size-1:
                    cur.next = que[0]   
        return root
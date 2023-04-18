# 题目：设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

# 思路：利用list很好实现，至于getMin()，每次都保存当前栈内的最小元素

# 解法
class MinStack:
    
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
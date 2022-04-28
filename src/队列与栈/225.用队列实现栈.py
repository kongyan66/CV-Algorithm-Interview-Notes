# 题目：请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）

# 思路1：采用两个队列，一个队列进行数据保存，另一个在pop进行数据复制(保证顺序）
class MyStack1:
    from collections import deque  #双向队列，popleft():向左出列  pop():向右出列  append(x):进列
    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x: int) -> None:
        self.queue_in.append(x)

    def pop(self) -> int:
      ‘’‘
        1. 首先判断是否为空
        2. 先把queue_in中的所有元素（除了最后一个），依次出列放进queue_out
        3. 交换in和out，此时out里只有一个元素
        4. 把out中的pop出来，即是原队列的最后一个
      
      ’‘’
        if self.empty():
            return None
        for i in range(len(self.queue_in)-1):
            self.queue_out.append(self.queue_in.popleft())
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        return self.queue_out.popleft()
        
    def top(self) -> int:
        if self.empty():
            return None
        return self.queue_in[-1]   # 说明deque双向队列可以直接索引


    def empty(self) -> bool:
        return len(self.queue_in) == 0
 
# 思路2： 采用一个队列，通过popleft保证输出顺序
class MyStack:
    from collections import deque
    def __init__(self):
        self.queue = deque()
    

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()
        
    def top(self) -> int:
        if self.empty():
            return None
        return self.queue[-1]


    def empty(self) -> bool:
        return not self.queue



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

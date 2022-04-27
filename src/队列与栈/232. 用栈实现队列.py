# 题目：请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）
# 思路：可以用List作为容器，一个输入栈，一个输出栈
# 讲解：https://programmercarl.com/0232.%E7%94%A8%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97.html#%E6%80%9D%E8%B7%AF
class MyQueue:
    def __init__(self):
      # in主要负责push，out主要负责pop
      self.stack_in = []
      self.stack_out = []

    # 有新元素进来，就往in里面push
    def push(self, x: int) -> None:
      self.stack_in.append(x)
   
    def pop(self) -> int:
      if self.empty():
        return None
      if self.stack_out:
        return self.stack_out.pop()  # list.pop(index=-1) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
      else:
        for i in range(len(self.stack_in)):
          self.stack_out.append(self.stack_in.pop())  # 保证先进的数在stack_out列表的末尾
        return self.stack_out.pop()

    def peek(self) -> int:
      ans = self.pop()
      self.stack_out.append(ans)
      return ans


    def empty(self) -> bool:
      return not (self.stack_in or self.stack_out)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

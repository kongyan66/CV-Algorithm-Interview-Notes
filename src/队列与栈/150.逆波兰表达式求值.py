# 题目：有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式
# 其实也是计算机的计算思路
# 考察：栈
# 思路：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      stack = []

      for item in tokens:
        if item in ['+', '-', '*', '/']:
          a = stack.pop()
          b = stack.pop()
          c = int(eval(f'{b}{item}{a}'))   # 注意除法要保留整数部分，所以在这用int()
          stack.append(c)
        else:
          stack.append(item)
        
      return int(stack.pop())

# 这个写法有个出错的地方
# int(a/b) 与(a//b) 有区别吗? 确实有，当结果为正数时确实没啥区别，但为负时，比如：-0.2 前者结果为0
# 而后者结果却为-1， 需要注意呀，不然想死也不知道哪出错了
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      stack = []

      for item in tokens:
        if item in ['+', '-', '*', '/']:
          a = stack.pop()
          b = stack.pop()
          if item == '+' : c = a + b
          elif item == '-': c = b - a
          elif item == '*': c = a * b
          elif item == '/': c = b / a    # 若为 b // a 则不通过
          stack.append(int(c))
        else:
          stack.append(int(item))
        
      return stack.pop()
# 题目：一共有三根柱子，用栈将所有盘子从第一根柱子移到最后一根柱子
# 思路：递归
'''
假设 n = 1,只有一个盘子，很简单，直接把它从 A 中拿出来，移到 C 上；
如果 n = 2 呢？这时候我们就要借助 B 了，因为小盘子必须时刻都在大盘子上面，共需要 4 步
如果 n > 2 呢？思路和上面是一样的，我们把 n 个盘子也看成两个部分，一部分有 1 个盘子，另一部分有 n - 1 个盘子。
'''

# 解法一：递归法
class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        n = len(A)
        self.recursion(n, A, B, C)

    def recursion(self, n, A, B, C):
       
        if n == 1:
            C.append(A[-1])
            A.pop()
            return 
        self.recursion(n-1, A, C, B)   # 将A上面n-1个通过C移到B
        C.append(A[-1])                # 将A最后一个移到C
        A.pop()                        # 这时，A空了
        self.recursion(n-1, B, A, C)   # 将B上面n-1个通过空的A移到C
        
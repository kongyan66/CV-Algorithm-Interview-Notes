# 题目:给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧, 返回窗口中的最大值
# 难度：困难
# 思路：单调队列

class MyQueue:
    def __init__(self):
        self.queue = []
     #如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。
    #这样就保持了队列里的数值是单调从大到小的了。
    def push(self, value):
        while self.queue and value >self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)
    #每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。
    #同时pop之前判断队列当前是否为空。
    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.pop(0)
    #查询当前队列里的最大值 直接返回队列前端也就是front就可以了。
    def front(self):
        return self.queue[0]
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MyQueue()
        res = []
        for i in range(k):  #先将前k的元素放进队列
            que.push(nums[i])
        res.append(que.front()) #result 记录前k的元素的最大值
        for i in (k, len(nums)):
            que.pop(nums[i-k])  #滑动窗口移除最前面元素
            que.push(nums[i])   #滑动窗口前加入最后面的元素
            res.append(que.front())  #记录对应的最大值
        return res
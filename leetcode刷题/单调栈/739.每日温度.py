# 题目：给一个数组tem, 表示每一天的温度，返回值answer[i]表示对于第i天来说，几天后温度会升高
# 思路：通常是一维数组，要寻找任一个元素的右边或者左边第一个比自己大或者小的元素的位置，此时我们就要想到可以用单调栈了。
'''
1.单调栈里放什么元素
放下标比较好，算距离方便，还能直接取值
2.单调栈里是递增还是递减(栈底到栈头)
此题是找右边比自己大的位置，那么需要监控的就是这种情况，所以栈内部要反着来，是递减的
3.确定入栈和出栈的条件
无非有三种 遍历元素的值T[i] 大于、小于、等于 栈顶的值stack[-1]
- stack[-1] >= T[i]
入栈
- stack[-1] < T[i]
先出栈，计算距离，直到符合入栈条件

'''
# 解法一：暴力法 超时 O(n^2)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            tem = 1
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    answer[i] = tem
                    break
                else:
                    tem += 1
        return answer

# 解法二：单调栈 O(N)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        res = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            # 如果当前值大于栈顶值，弹出，计算距离
            while stack and temperatures[stack[-1]] < temperatures[i]:
                # 出栈
                cur = stack.pop()
                # 计算距离
                res[cur] = i - cur
            # 入栈
            stack.append(i)
        return res
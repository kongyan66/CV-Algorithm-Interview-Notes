# 题目：n 个孩子站成一排，数组 ratings 表示每个孩子的评分。每个孩子至少分配到 1 个糖果，
# 相邻两个孩子评分更高的孩子会获得更多的糖果， 问需要多少颗糖

# 思路：这里需要用到两次贪心算法。
# 第一次从左向右遍历，局部最优：只要右边评分比左边大，右边的孩子就多一个糖果，全局最优：相邻的孩子中，评分高的右孩子获得比左边孩子更多的糖果
# 第二次从右向左遍历，同上

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1] * len(ratings)
        # 从左向右遍历 先考虑右边大于左边的情况
        for i in range(len(ratings)-1):
            if ratings[i] < ratings[i+1]:
                candy[i+1] = candy[i] + 1
      
        # 从右向左遍历 再考虑左边大于右边的情况
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                # 这里需要特别注意，我们不知道candy[i-1] 和candy[i]+1 谁个大，根据贪心准则，所以用max()去选择
                candy[i-1] = max(candy[i-1], candy[i]+1)
               
        return sum(candy)
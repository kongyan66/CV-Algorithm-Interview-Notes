# 题目：给你一个数组 points ，返回引爆所有气球所必须射出的 最小 弓箭数 。

# 思路：局部最优：当气球出现重叠，一起射，所用弓箭最少。全局最优：把所有气球射爆所用弓箭最少。

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        nums = 1
        for i in range(1, len(points)):
            # 相邻存在交集
            if points[i][0] <=  points[i-1][1]:
                # 更新下右边界，至于为什么选min,这是要判断交集是否连续，最短右边界都连续，长的必然也连续
                points[i][1] = min(points[i-1][1], points[i][1])
            # 相邻无交集
            else:
                nums += 1
        return nums
# 题目：以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

# 思路：按照左边界排序，排序之后局部最优：每次合并都取最大的右边界，这样就可以合并更多的区间了，整体最优：合并所有重叠的区间。

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 按左区间排序
        intervals.sort(key=lambda x:x[0])
        result = []
        start = 0
        end = 0
        for i in range(0, len(intervals)):
            # 没有交集，当前集合直接加入
            if not result or result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            # 有交集进行合并
            # 这里直接对result的值进行操作，原intervals只读
            # 之前想维护start, end的值，没有这样方便
            elif result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])      
        return result    
    
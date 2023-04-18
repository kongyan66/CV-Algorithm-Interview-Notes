# 题目：给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重叠 。

# 可以先求非交叉区间的数量，最后用区间总数一减就得到要移除区间额数量了，这样情况简单些
# 局部最优：优先选右边界小的区间，所以从左向右遍历，留给下一个区间的空间大一些，从而尽量避免交叉。全局最优：选取最多的非交叉区间。
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        num = 1
        # 对右区间区间进行排序，然后从左向右遍历
        intervals = sorted(intervals, key = lambda x:x[1])
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                num += 1
                end = intervals[i][1]
        return len(intervals) - num

# 本题其实和452.用最少数量的箭引爆气球非常像，弓箭的数量就相当于是非交叉区间的数量，
# 只要把弓箭那道题目代码里射爆气球的判断条件加个等号（认为[0，1][1，2]不是相邻区间），
# 然后用总区间数减去弓箭数量 就是要移除的区间数量了。
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        nums = 1  # 不重叠区间数量
        for i in range(1, len(intervals)):
            # 有重叠，更新下end
            if intervals[i][0] < intervals[i-1][1]:
                intervals[i][1] = min(intervals[i-1][1], intervals[i][1])
            # 无重叠，区间树加一
            else:
                nums += 1
        return len(intervals) - nums
      

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        count = 1
        
        x_end = intervals[0][1]
        for intter in intervals:
            start = intter[0]
            if start >= x_end:
                count += 1
                x_end = intter[1]
        return count
 

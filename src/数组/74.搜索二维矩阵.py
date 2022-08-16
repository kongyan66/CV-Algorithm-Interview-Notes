# 题目：编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。

# 解法一：暴力解法 未利用特性 时间复杂度O(m*n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False

# 解法二：一次二分查找  时间复杂度O(logmn)
# 将矩阵按行拼接刚好构成一个排好序的一维数组，满足二分查找的使用条件
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n -1  
        while left <= right:
            mid = (left + right) // 2
            # 映射到二维数组的位置，按行拼接的，所以对行数操作，其他步骤和二分查找完全一致
            # 如果是按列展开及对列数操作
            row, col = mid // n, mid % n  
            if matrix[row][col] > target:
                right = mid - 1
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                return True
        return False

# 解法三：二次二分法
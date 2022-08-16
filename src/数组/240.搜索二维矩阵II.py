# 题目：编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。（与74.搜索矩阵前一行末尾元素小于下一行首位元素）

# 思路：二分法要求数组有序，大了往右偏，小了往左偏，总可以找到目标值
# 而改题总右上角出发，向左变小，向右变大，符合二分法这种思路

# 解法
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # 从右上角出发，也可以左下角
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
        return False


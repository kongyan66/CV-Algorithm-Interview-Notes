# 题目：编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。（与74.搜索矩阵前一行末尾元素小于下一行首位元素）

# 思路：二分法要求数组有序，大了往右偏，小了往左偏，总可以找到目标值
# 该题总右上角出发，向左变小，向下变大，符合二分法思想

# 解法一：根据矩阵特点进行二分法 O(m + n)
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

# 解法二：每行进行二分法查找 O(mlog(n))
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if self.find(matrix[i], target):
                return True
        return False

    def find(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1
        return False

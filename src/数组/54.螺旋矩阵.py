# 题目：给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

# 思路：与59.基本一致，区别是该矩阵不是方阵，所以需要求loop和奇数情况下填补剩下部分有别

# 解法
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix),len(matrix[0])
        start_x, start_y = 0, 0   # x水平方向，y垂直方向
        loop = mid = min(row, col) // 2
        res = [0] * (row * col)  # 提前分配好，避免频繁重新分配空间
        count = 0
        for offset in range(1, loop+1):
            # 从左到右，左开右闭
            for j in range(start_x, col - offset):
                res[count] = matrix[start_x][j]
                count += 1
            # 从上到下，左闭右开
            for i in range(start_y, row - offset):
                res[count] = matrix[i][col - offset]
                count += 1
            # 从右到左，左闭右开
            for j in range(col -offset, start_x, -1):
                res[count] = matrix[row - offset][j]
                count += 1
            # 从下到上，左闭右开
            for i in range(row - offset, start_y, -1):
                res[count] = matrix[i][start_y]
                count += 1
            # 更新起始点  
            start_x += 1
            start_y += 1
        
        # 如果min(row, col)为奇数，需要单独处理矩阵中间位置
        if min(row, col) % 2 == 1:
            # 如果行数大于列数，剩余一块是垂直向下的长条，画个图就知道了
            if row > col:
                for i in range(mid, mid + row - col + 1):
                    res[count] = matrix[i][mid]
                    count += 1
            else: 
                for j in range(mid, mid + col -row + 1):
                    res[count] = matrix[mid][j]
                    count += 1
        return res


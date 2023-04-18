# 题目：给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。原地旋转，不能借助外援

# 思路：旋转涉及操作：转置和镜像(左右，上下)
'''
情况一：顺时针转 90 度：先转置再左右镜像
情况二：顺时针转 180 度:先上下镜像，再左右镜像（先左右再上下也可）
情况三：顺时针转 270 度：先转置再上下镜像
'''

# 解法一：顺时针旋转90度
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 先沿对角线反转，再翻转每一行
        row = len(matrix)
        # 转置
        for i in range(row):
            for j in range(i):  # 注意j的范围，如果j的范围也是0到n-1那么会出现交换后又交换回来 等于没有交换
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 左右镜像
        for i in range(row):
            matrix[i] = matrix[i][::-1]

# 变形一：如果是逆时针旋转90度呢
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 先沿对角线反转，再翻转每一行
        n = len(matrix)
        # 副对角线转置
        for i in range(n):
            for j in range(n - i):  # 注意j的范围，画个图好理解
                matrix[i][j], matrix[n - j - 1][n - i - 1] = matrix[n - j - 1][n - i - 1], matrix[i][j]
        # 左右镜像
        for i in range(n):
            matrix[i] = matrix[i][::-1]

# 变形三：上下对称
        for j in range(len(matrix[0])):
            for i in range(len(matrix) // 2):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n -i -1][j], matrix[i][j]

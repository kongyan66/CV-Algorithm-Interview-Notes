# 题目：给你几个物品，有重量和价值两个属性，还有一个容量为n的背包，问如何这些物品(唯一，只能放一次）放入背包中从而获得最大的价值。

'''
1. dp[i][j]表示物品标号为0-i放入容量为j的背包中得到的最大价值
2. 得到dp[i][j]有两种情况：1.不放入物品i 2.放入物品i 两个情况取价值最大的一种
   情况一：价值=dp[i-1][j]
   情况二：价值=放入i-1的价值 + 物品i的价值 = dp[i-1][j-weight[i]] + value[i]
   为啥减去weight[i]呢？这是我为了保证物品i一定能放进去
3.初始化dp, 二维数组一般初始化上边条和左边条，具体值代入推导下
4.遍历顺序：正反序都可以
5.打印输出dp
'''
def test_01_bag_problem(bag_size, weight, value):
    row, col = len(value), bag_size + 1
    dp = [[0] * col for _ in range(row)]

    # 初始化dp数组
    for i in range(row):
        dp[i][0] = 0
    fist_item_weight, fist_item_value = weight[0], value[0]
    for j in range(col):
        if j >= fist_item_weight:
            dp[0][j] = fist_item_value
    for i in range(row):
        for j in range(col):
            # 如果包的容量小于当期物品的重量，则不放入
            if j < weight[i]:
                dp[i][j] = dp[i-1][j]
            # 放入
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])
    return dp[row-1][col-1]

if __name__ == '__main__':
    bag_size = 4
    weight = [1, 3, 4]
    value = [15, 20, 30]
    res = test_01_bag_problem(bag_size, weight, value)
    print(res)
        
# 题目：给你几个物品，有重量和价值两个属性，还有一个容量为n的背包，问如何这些物品放入背包中从而获得最大的价值。
# 相比使用二维数组做状态转换，采用滚动数组更加简洁，空间复杂度降低，就是没那么直观了

'''
1. dp[j]表示容量表为j的背包所背物品最大价值
2. 得到dp[j]有两种情况：1.不放入物品i 2.放入物品i 两个情况取价值最大的一种
   情况一：价值=dp[j]
   情况二：价值=放入i-1的价值 + 物品i的价值 = dp[j-weight[i]] + value[i]
   为啥减去weight[i]呢？这是我为了保证物品i一定能放进去
   此时，dp[j]有两个选择：一个是取自己dp[j] 相当于 二维dp数组中的dp[i-1][j]，即不放物品i，
   一个是取dp[j - weight[i]] + value[i]，即放物品i，指定是取最大的，毕竟是求最大价值，
   dp[j] = max(dp[j], dp[j-weight[i]] + value[i])
3.初始化dp, 二维数组一般初始化上边条和左边条，具体值代入推导下
4.遍历顺序：背包逆序 倒序遍历是为了保证物品i只被放入一次
如果正序的话，发现前一个物品会被后一个物品再加一次，不理解了自己推导一遍就知道了
5.打印输出dp
'''
def test_01_bag_problem(bag_size, weight, value):

    # 初始化dp数组
    dp = [0] * (bag_size+1)

    for i in range(len(weight)):
        for j in range(bag_size, weight[i]-1, -1):
            dp[j] = max(dp[j], dp[j-weight[i]] + value[i])
    return dp[bag_size]

if __name__ == '__main__':
    bag_size = 4
    weight = [1, 3, 4]
    value = [15, 20, 30]
    res = test_01_bag_problem(bag_size, weight, value)
    print(res)
        
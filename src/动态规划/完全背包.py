# 题目：给你几个物品，有重量和价值两个属性，还有一个容量为n的背包，问如何这些物品(不唯一，可以无限放）放入背包中从而获得最大的价值。
# 和01背包最大区别是: 遍历背包的顺序，前者是从大到小遍历（避免重复多放），后者是前从小到大遍历(就是要重复放嘛)，所以代码就改这
# 另一个需要注意的是物品和背包的遍历内外层顺序是否可变，对于01背包是可以任意替换的，这里对于纯完全背包也是一样（可不可变看是否影响状态转换）
# 但有些题目做了变化是不可变的

# 也是动规五大步，这里省略
# 外：物品 内：背包
def test_complete_pack1(weight, value, bag_size):
    dp = [0] * (bag_size + 1)
    dp[0] = 0
    for i in range(len(weight)):
        for j in range(weight[i], bag_size+1, 1):
            dp[j] = max(dp[j], dp[j-weight[i]] + value[i])
    return dp[bag_size]

# 外：背包 内：物品
def test_complete_pack2(weight, value, bag_size):
    dp = [0] * (bag_size+1)
    dp[0] = 0
    for j in range(bag_size + 1):
        for i in range(len(weight)):
            if j >= weight[i]:
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    return dp[bag_size]
if __name__ == "__main__":
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_size = 4
    max_value = test_complete_pack2(weight, value, bag_size)
    print(max_value)
def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)

    # base case
    dp[0] = 0
    # 外层遍历所有状态的所有取值
    for i in range(amount + 1):
        # 内层for循环在求所有选择的最小值
        for coin in coins:
            # 子问题无解跳过
            if i - coin < 0:
                continue
            dp[i] = min(dp[i], dp[i -coin] + 1)
    return dp[-1]

if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    ans = coinChange(coins, amount)
    print(ans)



def coinChange(coins, amount):
    return dfs(coins, amount)

def dfs(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    res = float('inf')
    for coin in coins:
        subProblem = dfs(coins, amount - coin)
        if subProblem == -1:
            continue
        res = min(res, subProblem + 1)
    return res

if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    ans = coinChange(coins, amount)
    print(ans)

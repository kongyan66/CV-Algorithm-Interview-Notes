def shipWithDays(weight, d):
    # 最小载重量的范围就是在[sum_weight, max_weight]
    sum_weight = sum(weight)
    max_weight = max(weight)
    # 利用最小二分法找最小的k
    left, right = max_weight, sum_weight
    while left < right:
        mid = (left + right) >> 1
        if canShip(weight, d, mid):
            right = mid
        else:
            left = mid + 1

    return left
# 判断当前载重量k是否能在期限d天内运送完
# 利用贪心算法，每次都尽可能装满，看是否能按期运完
def canShip(weight, d, k):
    cur = k
    for i in range(len(weight)):
        if weight[i] > k:  # 说明一个也装不下
            return False
        if cur < weight[i]: # 装满了就换下一趟
            cur = k
            d -= 1
        # 贪心：一趟尽可能装满
        cur -= weight[i]
    return d > 0

if __name__ == '__main__':
    weights = [1,2,3,4,5,6,7,8,9,10]
    print(shipWithDays(weights, 5))

            


    

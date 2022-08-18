# 题目：给一个数数arr和看，返回arr中最小的k个数，且不能重复

# 思路：排序 + 去重

# 解法
def solution(arr, k):
    arr.sort()
    res = [arr[0]]
    for i in range(1, len(arr)):
        if len(res) == k:
            break
        if arr[i] != res[-1]:
            res.append(arr[i])
    return res

if __name__ == '__main__':
    # arr = [4, 4, 5, 1, 6, 2, 7, 3, 8]
    # k = 5
    recieve = list(map(int, input().split(',')))
    k = recieve[0]
    arr = recieve[1:]
    res = solution(arr, k)
    print(','.join(map(str, res)))

        
 
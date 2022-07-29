


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def longestarr(arr):
    if arr == None or len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 1
    length = len(arr)
    max_value = 1
    dp = [1] * length

    for i in range(1, length):
        if arr[i] > arr[i-1]:
            dp[i] = dp[i-1] + 1
        max_value = max(max_value, dp[i])
    return max_value


def findmin(arr):
    length = len(arr)
    ids = [0] * length
    for i in range(length):
        val = arr[i]
        arr[i] = (val, i)
    arr.sort()
    for i in range(length):
        ids[i] = arr[i][1]
    
    max_value = longestarr(ids)
    res = length - max_value
    return res
if __name__ == "__main__":
    import sys
    # for line in sys.stdin:
    #     a = line.split()
    arr_ = input()
    arr = [int(n) for n in arr_.split()]
    res = findmin(arr)
    print(res)
  
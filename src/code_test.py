def max_interval(arr):
    arr.sort(key = lambda x:x[1])
    end = arr[0][1]
    ans, count = 0, 0             # 记录相交区间数量
    for i in range(1, len(arr)):
        if end >= arr[i][0]: # 说明有交集，计数加一
            count += 1      
        else:               # 没有交集，更新end，清零count,有交集再重新计算。
            end = arr[i][1]
            count = 0
        ans = max(ans, count)
    return ans

def max_not_interval(arr):
    arr.sort(key = lambda x:x[1])
    end = arr[0][1]
    count = 1                     # 记录不相交区间数量，至少有一个区间不相交
    for i in range(1, len(arr)):
        if end <= arr[i][0]:
            count += 1    # 找到下一个选择区间了
            end = arr[i][1]
    return count

def is_interval(arr):
    arr.sort(key = lambda x:x[1])
    end = arr[0][1]

    for i in range(1, len(arr)):
        if end > arr[i][0]:
            return True
        else:
            end = arr[i][1]
    return False
    
if __name__ == '__main__':
    # arr = [[1, 3], [0, 4], [2, 5], [6, 7], [4, 8]]
    arr = [[1, 2], [3, 4], [3, 6]]
    res = is_interval(arr)
    print(res)
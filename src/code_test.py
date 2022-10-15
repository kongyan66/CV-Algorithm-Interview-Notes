# n, k = list(map(int, input().split()))
# nums = list(map(int, input().split()))
# nums.sort()

# i = n - 1
# while nums[i] - nums[0] > k:
#     i -= 1
# j = 0

# while nums[len(nums) - 1] - nums[j] > k:
#     j += 1
# ans = max(i + 1, n - j)
# print(ans)

# n, k = list(map(int, input().split()))
# nums = list(map(int, input().split()))

# nums.sort()
# dp = [0] * n
# dp[0] = 1

# for i in range(1, n):
#     if nums[i] - nums[i-1] <= k:
#         dp[i] = max(dp[i], dp[i - 1]+ 1)
 
# print(dp)

# n = int(input())
# start = list(map(int, input().split()))
# end = list(map(int, input().split()))

# arr = [[0] * 2 for _ in range(n)]
# for i in range(n):
#     arr[i][0] = start[i]
#     arr[i][1] = end[i]
arr = [[4,4], [1,1], [3, 3], [2, 3], [1, 2], [2, 2]]
path = []
res = []
count = 0

def dfs(arr, startindex):
    global count
    if len(path) == 3:
        if not is_overlap(path):
            count += 1
            res.append(path.copy())
        return
    
    for i in range(startindex, len(arr)):
        path.append(arr[i])
        dfs(arr, i + 1)
        path.pop()

def is_overlap(path):
    tem = path.copy()
    tem.sort(key = lambda x:x[1])
  
    for i in range(1, len(tem)):
        if tem[i][0] <= tem[i - 1][1]:
            return True
    return False
        
dfs(arr, 0)

print(count)
print(res)


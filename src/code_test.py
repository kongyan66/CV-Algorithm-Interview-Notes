n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
count = 0
# for i in range(1, len(arr2)):
#     if arr2[i] > arr2[i-1]:
#         count += 1
# print(count)
map = dict()
for i in range(len(arr1)):
    map[arr1[i]] = i

for j in range(len(arr2)-1):
    if map[arr2[i]] > map[arr2[i+1]]:
        count += 1

print(count)





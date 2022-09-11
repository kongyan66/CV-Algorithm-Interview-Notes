# n = int(input())
# arr = list(map(int, input().split()))
# # n = 3
# # arr = [2, -1, -1]
# count = 0
# sum = 0

# for i in range(n):
#     sum += arr[i]
#     if sum == 0:
#         sum += 1
#         count += 1
#     if arr[i] == 0:
#         arr[i] += 1
#         sum += 1
#         count += 1
# print(count)

t = int(input())

for _ in range(t):
    n, x, y, k = list(map(int, input().split()))
    x_time = k / x 
    y_time = (n - k + 1) / y

    if x_time == y_time:
        print("Tie")
    elif x_time < y_time:
        print("Win")
    else:
        print("Lose")

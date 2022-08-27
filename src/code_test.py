
'''
小美有一个精致的珠宝链子。初始这个链子上有n个宝石，从左到右分别编号为1~n （宝石上的编号不会因为交换位置而改变编号）。
接着，小美为了美观对这个项链进行微调，有m次操作，每次选择一个编号 x ,将编号 x 的宝石放到最左边（不改变其他宝石的相对位置）。
小美想知道，所有操作完成后最终链子从左到右宝石编号是多少。
'''
# timeout
# m, n = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))

# arr1 = [i for i in range(1, m + 1)]
# for i in range(n):
#     arr1.remove(arr2[i])
#     arr1.insert(0, arr2[i])

# print(' '.join(map(str, arr1)))
# timeout
m, n = 5, 3
arr2 = [2, 3, 4]

arr1 = [i for i in range(1, m+ 1)]
for i in arr2:
    index = i - 1
    while index >= 1:
        arr1[index], arr1[index -1] = arr1[index -1], arr1[index]
        index -= 1
print(arr1)

'''
有一个串S，问是否能将其划分成m个不相交的连续子串，使得这些连续子串可以与要求的连续子串一 一对应。两个串相对应是指这两个串完全相等。例如"aab"="aab" 但 "aab"≠"baa"

'''
m, n = list(map(int, input().split()))
s1 = input()
arr = list(map(int, input().split()))
s2 = []
for _ in range(len(arr)):
    s2.append(input())

print(s2)
    





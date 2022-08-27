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
    
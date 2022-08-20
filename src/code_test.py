# 1
# import math
# while True:
#     try:
#         m, n = map(int, input().split())
#         sum_ = 0
#         for i in range(m):
#             sum_ += m
#             m = math.sqrt(m)
#         sum_ = round(sum_, 2)
#         print(sum_)
#     except:
#         break
# # 2
# m, n = map(int, input().split())

# for i in range(m, n+1):
#     a, b, c = i % 10, i / 10 % 10, i % 100
#     print(a, b, c)

    
# '''
#  小团想要自己来烤串！不过在烤串之前，需要串好烤串。小团有n个荤菜和n个素菜，他想按顺序分别一个荤菜一个素菜串起来，想请你帮他串好！
# 给出两个长度分别为n的仅包含小写英文字母的串A和B，分别代表荤菜和素菜的种类（用字母来表示菜的种类）。
# 请你以从左到右的顺序依次串好他们！例如对于荤菜串A1A2...An和素菜串B1B2...Bn，串好应该是A1B1A2B2...AnBn
# '''
# # n = int(input())
# # str1 = input()
# # str2 = input()
# # str_list = []
# # for i in range(n):
# #     str_list.append(str1[i])
# #     str_list.append(str2[i])
# # print(''.join(str_list))


# n = int(input())
# s1 = list(map(int, input().split()))
# s2 = list(map(int, input().split()))
# s3 = list(map(int, input().split()))
# ans = list(map(int, input().split()))

# res = []
  
# for i in range(n):
#     for j in range(n):
#         a1 = abs(i - s1[0]) + abs(j - s1[1])
#         a2 = abs(i - s2[0]) + abs(j - s2[1])
#         a3 = abs(i - s3[0]) + abs(j - s3[1])

#         if a1 == ans[0] and a2 == ans[1] and a3 == ans[2]:
#             res.append([i,j])
# res.sort()
# print(''.join(map(str, res[0])))




# 

n, m = list(map(int, input().split()))
pro = list(map(int, input().split()))
# pro = pro / 100
score = [(int(x), idx) for idx, x in enumerate(input().split())]
score.sort(key = lambda x:x[0])
score.reverse()
ans = 0
for idx, sc in enumerate(score):
    if idx < m:
        ans += sc[0]
    else:
        ans += sc[0] * pro[sc[1]] / 100
print(round(ans, 2))

 



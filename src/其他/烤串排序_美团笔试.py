'''
小团想要自己来烤串！不过在烤串之前，需要串好烤串。小团有n个荤菜和n个素菜，他想按顺序分别一个荤菜一个素菜串起来，想请你帮他串好！
给出两个长度分别为n的仅包含小写英文字母的串A和B，分别代表荤菜和素菜的种类（用字母来表示菜的种类）。
请你以从左到右的顺序依次串好他们！例如对于荤菜串A1A2...An和素菜串B1B2...Bn，串好应该是A1B1A2B2...AnBn
'''
# 解：比较简单，就是交错合并字符串
n = int(input())
str1 = input()
str2 = input()
str_list = []
for i in range(n):
    str_list.append(str1[i])
    str_list.append(str2[i])
print(''.join(str_list))

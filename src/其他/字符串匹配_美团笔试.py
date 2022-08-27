'''
2022/08/27 01
小美在摆弄她的字符串。最近小团送了小美一个特殊字符 ' * '，这个字符可以和其他所有字符匹配，除了这个字符外，其他字符只能自己和自己匹配。
小美先前有一个字符串S，长度为n，现在她又新组合了一个可有特殊字符 ' * ' 的字符串s，长度为m。小美想知道有多少个位置 i，
使得S[i+j]与s[j]对于1≤j≤m均能匹配上？其中X[y]代表字符串X中第y位的字符。
'''
# m, n = 7, 3
# s1 = "abcaacc"
# s2 = "a*c"
# count = 0
# tem = 0
# for i in range(len(s1)):
#     for j in range(len(s2)):
#         if s1[i + j] == s2[j] or s2[j] == "*":
#             tem += 1
#         else:
#             break
#     if tem == n:
#         count  += 1
#         tem = 0
# print(count)
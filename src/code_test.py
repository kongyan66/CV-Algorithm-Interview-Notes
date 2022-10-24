#-*- coding: utf-8 -*-

# BRANKETS = {'}':'{',']':'[',')':'('}
# BRANKETS_LEFT, BRANKETS_RIGHT = BRANKETS.values(), BRANKETS.keys()

# def bracket_check(string):
#     """括号匹配检测函数"""
#     stack = []
#     for char in string:
#         # 如果是左括号
#         if char in BRANKETS_LEFT:
#             # 入栈
#             stack.append(char)
#         # 右括号
#         elif char in BRANKETS_RIGHT:
#             # stack不为空，并且括号匹配成功
#             if stack and stack[-1] == BRANKETS[char]:
#                 # 出栈
#                 stack.pop()
#             # 匹配成功
#             else:
#                 return False
    
#     return not stack

# def main():
#     print(bracket_check('{}'))
#     print(bracket_check('{brace*&^[square(round])end}'))

# if __name__ == '__main__':
#     main()



res = []
a = [1, 2, 3]
b = [4, 5, 6, 7]
map = sorted(zip(a, b))
print(map)

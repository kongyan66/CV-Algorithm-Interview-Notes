# 题目：f(x)可以求得x二进制最低位的值(从右到左，第一个1的位置）是多少，比如f(10)=2, 其中10=(1010)，求

import re


def solution(n):
    strs = list(bin(int(n)))
    strs_ = strs[::-1]
    index = len(strs_) - strs_.index('1') - 1  # 获取二进制数逆序中第一个1的索引
    new_str = ''.join(strs[index:])
    return int(new_str, 2)
    

if __name__ == "__main__":
    a = input()
    res = solution(a)
    print(res)

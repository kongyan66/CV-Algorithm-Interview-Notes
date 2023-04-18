# 题目：把字符串 s 中的每个空格替换成"%20"。

# 思路：双指针 由后向前填充
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = list(s)
        count = res.count(' ')
        res.extend([' ']*count*2)  # 原先有一个空格，所以只需要补充二个就好
        left, right = len(s) - 1, len(res) - 1  
        # 从后向前填充
        while left >= 0:
            # 左指针用于前面探路，遇到非空值就往后放（此地有一个值，右指针需要减一了），给填充值留位置，
            if res[left] != ' ':
                res[right] = res[left]
                right -= 1
            # 当左指针遇到空值，说明该填充了，此时右指针需要填充三个值（填完右指针位置减3）
            else:
                res[right-2:right+1] = "%20"  # 注意切片写法（左闭右开），所以右区间需要加一
                right -= 3
            left -= 1
        return ''.join(res)
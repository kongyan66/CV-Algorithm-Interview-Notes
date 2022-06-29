# 题目：正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
# 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。

# 思路：切割问题  

# 解法： 回溯
class Solution:
    def __init__(self):
        self.result = []
        self.pointNum = 0
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 标准IP地址长度最长为12（3*4）
        if len(s) > 12:
            return []
        self.backtracking(s, 0, 0)
        return self.result
    # 1.确定递归的入参与返回值
    def backtracking(self, s, startIndex):
        # 2.确定递归终止条件
        if self.pointNum == 3:
            # 验证最后一段IP块是否有效
            if self.is_valid(s, startIndex, len(s)-1):
                 self.result.append(s[:])
            return 
        # 3.单层搜索逻辑
        for i in range(startIndex, len(s)):
            if self.is_valid(s, startIndex, i):
                # 这里巧妙在直接对s进行操作，没有像之前用path单独保存，原因是我们每次保存的是一个完整的s
                s = s[:i+1] + '.' + s[i+1:]
                self.pointNum += 1
                self.backtracking(s, i+2) # 正常是i+1,为了跳过".",所以是i+2
                self.pointNum -= 1 # 回溯
                s = s[:i+1] + s[i+2:]  # 回溯 去掉.
            # 如果有一个ip块是不合法的，递归就停止
            else:
                continue  # break也可以，就是有点疑惑


    # 判断一个IP块是否合法，分三种情况
    # 不能以0开头
    # 不能有0-9之外的字符
    # 整形值不能大于255
    # def is_valid(self, s, start, end):
    #     if end > start:
    #         return False
    #     if s[start] == '0' and start != end:
    #         return False
    #     for i in range(start, end+1):
    #         if s[i] > '9' or s[i] < '0':
    #             return False
        
    #     if not 0 <= int(s[start:end]) <= 255:
    #         return False
    #     return True
    # 左闭右闭
    def is_valid(self, s: str, start: int, end: int) -> bool:
        # 这个也很关键，就是想不到这种情况
        if start > end:  
             return False
        # 若数字是0开头，不合法
        if s[start] == '0' and start != end:
            return False
        if not 0 <= int(s[start:end+1]) <= 255:
            return False
        # 注意以下写法不通过
        # if s[start, end+1] < '0' or s[start, end+1] > '255':
        #   return False
        return True
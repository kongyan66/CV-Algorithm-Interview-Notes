# 题目：请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
# 讲解：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/solution/mian-shi-ti-05-ti-huan-kong-ge-ji-jian-qing-xi-tu-/

# 暴力解法，使用辅助空间，最简单，空间复杂度O(N) 时间复杂度O(N)
class Solution1:
    def replaceSpace(self, s: str) -> str:
      res = []
      for i in s:
        if i == ' ':
          res.append("%20")
        else:
          res.append(i)
      s = "".join(res)
      return s

# 使用指针，在不新建字符串的情况下实现原地修改。但需要知道修改后列表的长度，
class Solution2:
    def replaceSpace(self, s: str) -> str:
        res = list(s)
        counter = s.count(" ")
        # 每碰到一个空格就多拓展两个格子，1 + 2 = 3个位置存’%20‘
        res.extend([' ']*counter*2)  # .extend(ListB)
        left = len(s) - 1
        right = len(res) - 1 

        while left >= 0:
          if res[left] != " ":      # 没有空格，就把当前值往后补   
            res[right] = res[left]
            right -= 1
          else:
            res[right-2:right+1] = "%20" # 有空格， 腾出三个位置
            right -= 3  
          left -= 1
        s = "".join(res)       # 列表转字符串
        return s
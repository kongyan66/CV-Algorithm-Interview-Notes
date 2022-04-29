# 题目：给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
# 考察：栈(优选)、双指针
# 思路：遍历所有字符串，依次存入栈，若当前值与前一个相等，则弹出前一个值，最后身剩下的就是不重复字母

class Solution1:
    def removeDuplicates(self, s: str) -> str:
      stack = []
       
      for item in s:
        if stack and item == stack[-1]:
          stack.pop()
        else:
          stack.append(item)
      res = ''.join(stack)
      return res

# 双指针：快指针前面探路，慢指针遇到重复数组后退，且交互快慢指针的值，就把不重复字符移到了前面
class Solution2:
    def removeDuplicates(self, s: str) -> str:
      s = list(s)
      length = len(s)
      fast = slow = 0

      while fast < length:
        s[slow] = s[fast]   # 把不重复的值往前放
        if slow > 0 and s[slow] == s[slow-1]:  # 遇到重复的往后退
          slow -= 1
        else:
         slow += 1
        fast += 1
      
      return ''.join(s[:slow])



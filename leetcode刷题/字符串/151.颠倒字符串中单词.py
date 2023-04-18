# 题目：给你一个字符串 s ，颠倒字符串中 单词 的顺序。字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。
# 考察：双指针 快慢指针 字符串综合应用
# 作法：如果用字符串拆分，用辅助内存存储就很简单，该题不希望使用额外内存，所以就只能对字符串下手，即空间复杂度为O(1)
# 思路：1.去除多余空格 2.反转整字符串列表 3.反转字符串中的单词
class Solution:
    def reverseWords(self, s: str) -> str:
      # 去除多余空格
      def del_extra_space(s):
        left = 0
        right = len(s) - 1
        # 空间双指针多靠while left<right驱动
        while left < right and s[left] == ' ':    # 去除头部空格
          left += 1
        while left < right and s[right] == ' ':   # 去除尾部空格
          right -= 1
        tem = []
        while left <= right:                      # 去除中间多余控空格
          if s[left] != ' ':
            tem.append(s[left])
          elif tem[-1] != ' ':                    # 只保上一个字符后的空格，这个条件也比较巧妙
            tem.append(s[left])
          left += 1
        return tem
      # 反转列表
      def reverse_list(s):
        left = 0
        right = len(s) - 1
        while left < right:
          s[left], s[right] = s[right], s[left]
          left += 1
          right -= 1
        return s
      # 反转单词， 重点是找到完整一个单词的区间
      def reverse_word(s):
          slow = 0
          fast = 0
          while fast < len(s):
            if s[fast] == ' ':  
              s[slow:fast] = reverse_list(s[slow:fast])  # 反转单词
              slow = fast + 1
            elif fast == len(s) - 1:  # 反转最后一个单词，由于切片索引只能到len(s)-1, 所以需要单独列出来，人工加一
              s[slow:fast+1] = reverse_list(s[slow:fast+1])
            fast += 1
          return s

      s = list(s)
      s = del_extra_space(s)
      s = reverse_list(s)
      s = reverse_word(s)
      s = ''.join(s)
      return s
# 题目：给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
# 思路：和242.有效字母位类似，

class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
      record = [0] * 26    # 26个字母，26个位置，说明空列表是无法直接赋值的
      for i in magazine:
        record[ord(i) - ord('a')] += 1      # 26个映射到数组里

      for i in ransomNote:
        if record[ord(i) - ord('a')] == 0:  
          return False
        else:
          record[ord(i) - ord('a')] -= 1
      return True

class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
      from collections import defaultdict

      hashmap = defaultdict(int)
      for i in magazine:
        hashmap[i] += 1
      
      for i in ransomNote:
        value = hashmap.get(i)
        if value == 0 or value is None:
          return False
        else:
          hashmap[i] -= 1

      return True
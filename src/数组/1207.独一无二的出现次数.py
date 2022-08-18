# 题目：给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。

# 思路：先用dict保证每个数出现的次数，再对次数进行排序，判断相邻之间是否有相等的，没有就返回True

# 解法一：hash表 + 排序
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = defaultdict(int)
        for num in arr:
            map[num] += 1

        map = sorted(zip(map.values(), map.keys()))  # 注意字典的排序，用zip将key于values互换，sorted返回的是列表类型
        for i in range(1, len(map)):
            if map[i-1][0] == map[i][0]:
                return False 
        return True


# 解法二：双hash表
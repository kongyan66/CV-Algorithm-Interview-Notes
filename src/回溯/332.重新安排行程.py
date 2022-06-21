# 题目：https://leetcode.cn/problems/reconstruct-itinerary/solution/shou-hua-tu-jie-liang-chong-jie-fa-zui-ji-ben-de-h/
# 说人话就是：你在肯尼迪机场，给你一匝机票，随便飞，最后告诉我你去往城市的路径（所以机票都得用完，且只能用用一次）

# 思路： 难题 dfs遍历，从JFK开始，尝试所有可能，再到相邻机场尝试以上步骤

# 解法一： 还是理解不很透彻，慢慢领悟吧
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 构建行程表，读出起点和终点
        tickets_dict = defaultdict(list)
        for item in tickets:
            tickets_dict[item[0]].append(item[1])
            
        path = ['JFK']

        def backtracking(start_point):
            if len(path) == len(tickets) + 1:
                return True
            # 字母升序排列
            tickets_dict[start_point].sort()
            # 一个起始点，也可能有多个目的地
            for _ in tickets_dict[start_point]:
                # 用掉了就删除，避免死循环
                end_point = tickets_dict[start_point].pop(0)
                # 找到一个相邻地，加入path
                path.append(end_point)
                # 
                if backtracking(end_point):
                    return True
                path.pop()  # 回溯  回退上一状态
                tickets_dict[start_point].append(end_point) # 回溯

        backtracking("JFK")
        return path
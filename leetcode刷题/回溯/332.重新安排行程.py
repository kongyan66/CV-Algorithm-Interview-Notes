# 题目：https://leetcode.cn/problems/reconstruct-itinerary/solution/shou-hua-tu-jie-liang-chong-jie-fa-zui-ji-ben-de-h/
# 说人话就是：你在肯尼迪机场，给你一匝机票，随便飞，最后告诉我你去往城市的路径（所以机票都得用完，且只能用用一次）

# 思路： 难题 dfs遍历，从JFK开始，尝试所有可能，再到相邻机场尝试以上步骤

# 解法一： 还是理解不很透彻，慢慢领悟吧
# 疑问一： 为啥tickets_dict[start_point].pop()输出不能通过，不是因为排序的问题
# 疑问二： 多条path怎么办呢

class Solution:
   
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 构建行程表，记录起点和终点，{key:start_point valuse:[end_point,]}
        tickets_dict = defaultdict(list)
        for item in tickets:
            tickets_dict[item[0]].append(item[1])
        # 必需从JFK出发  
        path = ['JFK']

        def backtracking(start_point):
            # 本题的result相当于39.求组合总和中的path，
            # 也就是本题的result就是记录路径的（就一条），在如下单层搜索的逻辑中result就添加元素了。
            if len(path) == len(tickets) + 1:
                return True

            tickets_dict[start_point].sort()   # 字母升序排列
            # DFS找所有路径
            for _ in tickets_dict[start_point]:
                end_point = tickets_dict[start_point].pop(0)  # 目的地用一次就删除，避免死循环
                path.append(end_point)               # 找到一个相邻地，加入path
                #  
                if backtracking(end_point):
                    return True
                path.pop()  # 回溯  回退上一状态
                tickets_dict[start_point].append(end_point) # 回溯

        backtracking("JFK")
        return path

# re-3
from collections import defaultdict
class Solution:
    def __init__(self):
        self.path = ["JFK"]
        self.tickets = []

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 构建行程表，读出起点和终点，{key:start_point valuse:[end_point,]}
        tickets_dict = defaultdict(list)
        self.tickets = tickets
        for ticket in tickets:
            tickets_dict[ticket[0]].append(ticket[1])
        
        self.backtracking(tickets_dict, 'JFK')

        return self.path
    
    def backtracking(self, tickets_dict, start_point):
        if len(self.path) == len(self.tickets) + 1:
            return True
        tickets_dict[start_point].sort()
        for _ in range(len(tickets_dict[start_point])):
            end_point = tickets_dict[start_point].pop(0)
            self.path.append(end_point)
            # 本题我们只需要一条符合条件的路径，找到即返回且结束所有递归
            if self.backtracking(tickets_dict, end_point):  
                return True
            self.path.pop()
            tickets_dict[start_point].append(end_point)
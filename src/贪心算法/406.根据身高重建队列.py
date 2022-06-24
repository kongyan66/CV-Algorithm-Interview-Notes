# 题目：重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。

# 思路：二个维度分别考虑
# 先按照身高h来排序，身高一定是从大到小排（身高相同的话则k小的站前面），让高个子在前面
# 然后只按照k为下标重新插入队列（这点不好理解）
# 局部最优：优先按身高高的people的k来插入。插入操作过后的people满足队列属性  全局最优：最后都做完插入操作，整个队列满足题目队列属性

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 先按照h维度的身高顺序从高到低排序。确定第一个维度
        # lambda返回的是一个元组：当-x[0](维度h）相同时，再根据x[1]（维度k）从小到大排序
        people = sorted(people, key=lambda x:(-x[0], x[1]))
        que = []
        # 根据每个元素的第二个维度k，贪心算法，进行插入
        # people已经排序过了：同一高度时k值小的排前面。
        for p in people:
            que.insert(p[1], p)   # 这块就很神奇
        return que
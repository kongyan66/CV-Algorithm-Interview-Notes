# 题目：考试即将来临，共有n道题，每道题有对应的分分值score，及得分的概率probality, 为了得高分
# 小明选择性复习m道题，复习过得分概率就为100%，问小明能得到的最高分是多少？

# 思路一：为保证最大收益，我们选择复习得分最高的题  但只ac了18%
n, m = list(map(int, input().split()))
pro = list(map(int, input().split()))
score = [(int(x), idx) for idx, x in enumerate(input().split())]  # 元组保存得分与原始位置(后面要排序打乱对于关系，所以得记住位置)
score.sort(key = lambda x:x[0], reverse=True)  # 递减排序
ans = 0
for idx, sc in enumerate(score):
    if idx < m: # 复习前m个分值最大的
        ans += sc[0]
    else:
        ans += sc[0] * pro[sc[1]] / 100  # 后面的没复习，所以要乘以正确的概率
print(round(ans, 2))  # 保留两位小数
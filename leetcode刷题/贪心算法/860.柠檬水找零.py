# 题目：柠檬水一杯五块，收到钱有5,10,20，给你一个整数数组bills，其中bills[i]是第i位顾客付的账。如果你能给每位顾客正确找零，返回true，否则返回 false 。

# 思路：此题无非有三种情况：
# 1.收到5美元， 无需找零
# 2.收到10美元， 消耗一个5，增加一个10
# 3.收到20美元， 优先消耗一个10,和一个5， 不行再用3个5

# 局部最优：遇到账单20，优先消耗美元10，完成本次找零。全局最优：完成全部账单的找零
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = {
            '5': 0,
            '10': 0,
            '20': 0
        }
        for m in bills:
            if m == 5:
                money['5'] += 1
            elif m == 10:
                money['10'] += 1
                if money['5'] >= 1:
                    money['5'] -= 1
                else:
                    return False
            elif m == 20:
                # 这里用到了贪心思想，优先用10去找零，因为5块的比较万能
                if money['10'] > 0 and money['5'] > 0:
                    money['20'] += 1
                    money['10'] -= 1
                    money['5'] -= 1
                elif money['5'] >= 3:
                    money['20'] += 1
                    money['5'] -= 3
                else:
                    return False
        return True

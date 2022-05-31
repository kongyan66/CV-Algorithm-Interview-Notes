# 题目：给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。

# 思路：最简单就是遍历所有节点，用map保存节点值及频率，最后再排序

# 解法一： 迭代法 通用写法   写法还是很臃肿
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        stack = []
        record = {}
        result = []
        output = []
        cur = root
        # 中序遍历
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if cur.val in record:
                    record[cur.val] += 1
                else:
                    record[cur.val] = 1
                cur = cur.right
        # dict -> list
        for key, val in record.items():
            result.append((key, val))
        # sorted(result, key=lambda result:result[1])  # 这种排序写法有问题
        result.sort(key=lambda x:x[1])  # 只对元组的第二个元素（频率）排序
        for i in range(len(result)):    # 获取频率最高的节点值
            if result[i][1] == result[-1][1]:
                output.append(result[i][0])
        return output   
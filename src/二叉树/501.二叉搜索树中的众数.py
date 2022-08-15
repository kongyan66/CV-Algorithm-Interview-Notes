# 题目：给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。

# 思路：最简单就是遍历所有节点，用map保存节点值及频率，最后再排序

# 解法一： 迭代法 通用写法   写法还是很臃肿
class Solution1:
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

# 解法二： 迭代法 考虑二叉搜索树特性  
# 得到是有序数组，所以如果重复出现的值必然是相邻的，所以count实时记录当前值出现的次数，把节点值先放入res中，如果出现频率更大的值，就清空res重新来
class Solution2:
    def findMode(self, root: TreeNode) -> List[int]:
        stack = []
        pre = None
        cur = root
        maxCount = 0 # 记最大频率
        count = 0  # 记当前值的最大频率
        res = []
       # 还是中序遍历
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre == None:    # 第一次count记1
                    count = 1
                elif pre.val == cur.val:
                    count += 1
                else :
                    count = 1
                if count == maxCount:
                    res.append(cur.val)
                if count > maxCount:
                    maxCount = count
                    res.clear()
                    res.append(cur.val)

                pre = cur
                cur = cur.right
        return res

# 递归法 采用中序遍历模板
# 模板小结
void searchBST(TreeNode* cur) {
    if (cur == NULL) return ;
    searchBST(cur->left);       // 左
    （处理节点）                // 中
    searchBST(cur->right);      // 右
    return ;
}

# 写法
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        pre = None
        count = 0
        maxCount = 0
        res = []
        
        def recursion(root):
            nonlocal pre 
            nonlocal count      # 记录当前频率
            nonlocal maxCount   # 记录最大频率
            nonlocal res        # 记录最终结果
            # 对每个节点出现次数进行统计
            if not root:
                return 
            recursion(root.left)

            cur = root
            # 计数器处理
            if not pre: # 首位默认为1
              count = 1
            elif cur.val == pre.val: # 连续加一
                count += 1
            else:
                count = 1  # 连续中断计数器归一
            pre = cur
            # 记录出现次数最多的节点
            if count == maxCount:
                res.append(cur.val)
            elif count > maxCount:
                res.clear()
                maxCount = count
                res.append(cur.val)

            recursion(root.right)

        recursion(root)
        return res
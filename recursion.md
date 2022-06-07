# 理解递归
## Motivation
为了更深刻理解递归的逻辑及写法，在这里收集一些典型的例子，努力早日掌握！！！
## 步骤
1.确定入参与返回值
2.确定终止条件
3.确定单层递归逻辑
## 疑惑点
- [] 如果把递归函数看做一个黑箱，怎么确定其功能（入参与出参）
- [] 递归逻辑不同题之间差异很大，也不好想

## 题目
- 144.二叉树前序遍历
'''pyhton
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 局部变量存放节点值
        res = []
        self.recursion(root, res)
        return res

    # 因为入参与上面函数不一致，所以只能分开写，后面会遇到很多合一起的
    # 1.确定入参与返回值
    # 入参就是欲处理的节点了（只去考虑一个节点，递归一次我们只处理一个节点）
    # 无返回值，因为我们需要的节点的值保存在一个单独的列表（局部变量）中，所以不需要返回任何值
    def recursion(self, node, res):
        # 2.确定终止条件
        # 因为无有效返回值，所以为了让递归停下来，我们返回一个空值。
        # 一方面保证递归及时停下来，这样后面的逻辑才不会报错；另一方面防止爆栈
        if node is None:
            return 
        # 3.确定单层递归逻辑
        # 前序遍历是中左右的循序，所以在单层递归的逻辑，是要先取中节点的数值，然后是左右
        res.append(node.val)
        self.recursion(node.left, res)
        self.recursion(node.right, res)
'''
- 104.二叉树最大深度
'''python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursion(root)
    # 1.确定入参与返回值
    # 返回值就是当前节点的深度depth
    def recursion(self, node):
        # 2.确定终止条件
        # 此题有返回值，故终止的时候也要有返回值（空节点深度为0）
        if not node:
            return 0
        # 3.确定单层递归逻辑
        # 分别求左右子树的深度，至于为啥不需要判断节点是否存在了，不存在深度就为0呗
        left_depth = self.recursion(node.left)
        right_depth = self.recursion(node.right)
        # 这里需要注意下，是从当前节点往下看，所以最终深度需要+1
        return max(left_depth, right_depth)+1
'''

- 111.二叉树最小深度
需要讨论三种情况
'''python
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 1.确定入参和出参
        return self.getdepth(root)

    def getdepth(self, node):
        # 2.确定停止条件
        if node is None:
            return 0
        # 3.确定单层递归逻辑
        left_depth = self.getdepth(node.left)
        right_depth = self.getdepth(node.right)
        # z这里容易出错：最小深度是从根节点到最近叶子节点的最短路径上的节点数量，如果左子叶无节点，深度并不一定是1
        # 如果左子叶为空，就看右子叶最小深度
        if node.right == None and node.left != None:
            return left_depth + 1
        # 如果右子叶为空，就看左子叶为空
        elif node.right != None and node.left == None:
            return right_depth + 1
        # 如果左右子节点均存在，看左右子叶的最小深度
        else:
            return min(left_depth, right_depth) + 1
'''
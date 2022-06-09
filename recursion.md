# 理解递归
## Motivation
为了更深刻理解递归的逻辑及写法，在这里收集一些典型的例子，努力早日掌握！！！

## 相关讲解

- [什么是递归](https://blog.ihuxu.com/recursive/)
  递归的特性:

  - 自身调用自身
  - 回溯时还原现场
    在使用递归方法时，其中有一个不得不提的特性——回溯时还原现场。通过递归调用，程序将执行到极限触达边界条件时，就需要将当前层的调用跳出“调用栈”，在跳出“调用栈”时，需要将一些状态信息还原到上一层场景所属的状态，即所谓的回溯时还原场景。

- [一只青蛙跳出来的分治法、回溯法](https://blog.ihuxu.com/divide-and-conquer-backtracking-and-dynamic-programming-from-a-frog-jumping-out/#comment-23330)
  分治法是解决规模庞大的问题的很好的思路，他通过降低问题的规模，形成若干个规模更小但形式相同的子问题，进行递归求解。在求解过后，将各个子问题的解合并起来，形成原问题的解。
  那么它的大致流程主要分成三步：

  - 分解（Divide）将大规模的问题分解成若干个规模更小但形式相同的子问题

  - 解决（Conquer）如果当前问题的规模足够小，并可以直接解决的话，那么直接解决并返回解。否则，继续进行分解并递归求解分解后的子问题。

  - 合并（Merge）将各个子问题合并，最终形成原问题的解。

  所以，明确了三步之后，还要明确一件事件——实现方式：递归法。
  我们往往看到的递归算法从广义上来说都是分治法。无非就是有些递归算法将问题分解了若干个子问题，然而有些递归算法将问题分解成了一个子问题。那么有些作者会称作前者是分治法，后者是减治法。
  其实，这个概念真的非常非常重要。在面对很多问题的时候，都可以用这种思路去思考。那么其中思考的一个非常重要的一点就是递归算法中的边界（跳出）条件的判定。

## 递归使用条件（还不深刻）

递归的本质就是`将原问题拆分成具有相同性质的子问题。`

递归的特点：
1、子问题拆分方程式，比如：f(n) = f(n-1) * n
2、终止条件：也就是子问题无法再进一步拆分时，这时可以直接求出解，退出递归。
一个问题能否使用递归求解，就看能不能满足上面两个特征。

## 一般步骤

1.确定返回值与参数
在定义一个递归函数前，我们必须清楚用这个递归函数干什么，我们得到是什么(返回值)，函数规模有多大（参数）
- 返回值  函数的含义，代表了递归函数能为我们解决什么样的问题
- 函数的参数 代表了递归函数求解的问题的规模

2.确定终止条件
3.确定单层递归逻辑
   这里其实干了两件事：1.该层逻辑实现 2.将递归传递下去

## 疑惑点
- [ ] 如果把递归函数看做一个黑箱，怎么确定其功能（入参与出参）
- [ ] 递归逻辑不同题之间差异很大，也不好想

## 递归与迭代（还不深刻）

归和迭代其实是天生一对的，本质是一样的，迭代只是`我们自己模拟了递归的调用栈而已`，因此迭代一般会用到`栈`这样的数据结构

## 相关题目
- 144.二叉树前序遍历
  
  ```python
  class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
       # 局部变量存放节点值
  ​      res = []
  ​      self.recursion(root, res)
  ​      return res
  
  # 因为入参与上面函数不一致，所以只能分开写，后面会遇到很多合一起的
  # 1.确定入参与返回值
  # 入参就是欲处理的节点了（只去考虑一个节点，递归一次我们只处理一个节点）
  # 无返回值，因为我们需要的节点的值保存在一个单独的列表（局部变量）中，所以不需要返回任何值
    def recursion(self, node, res):
         # 2.确定终止条件
         # 因为无有效返回值，所以为了让递归停下来，我们返回一个空值。
         # 一方面保证递归及时停下来，这样后面的逻辑才不会报错；另一方面防止爆栈
  ​      if node is None:
  ​          return 
         # 3.确定单层递归逻辑
         # 前序遍历是中左右的循序，所以在单层递归的逻辑，是要先取中节点的数值，然后是左右
  ​      res.append(node.val)
  ​      self.recursion(node.left, res)
  ​      self.recursion(node.right, res)
  ```
- 104.二叉树最大深度
  ```python
  class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursion(root)
    # 1.确定入参与返回值
    # 返回值就是当前节点的深度depth
    def recursion(self, node):
        # 2.确定终止条件
        # 此题有返回值，故终止的时候也要有返回值（空节点深度为0）
  ​      if not node:
  ​          return 0
        # 3.确定单层递归逻辑
        # 分别求左右子树的深度，至于为啥不需要判断节点是否存在了，不存在深度就为0呗
  ​      left_depth = self.recursion(node.left)
  ​      right_depth = self.recursion(node.right)
        # 这里需要注意下，是从当前节点往下看，所以最终深度需要+1
  ​      return max(left_depth, right_depth)+1
  ```

- 111.二叉树最小深度
   需要讨论三种情况
  ```python
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
  ```

- 101.对称二叉树

  ```python
  class Solution:
      def isSymmetric(self, root: Optional[TreeNode]) -> bool:
          if not root:
              return True
          # 1.确定入参和返回值
          # 入参就是两个树的根节点了
          # 返回值是判断当前节点是否镜像对称的bool值
          return self.recursion(root.left, root.right)
  
      def recursion(self, left_node, right_node):
          # 2.确定终止条件
          # 有必然四种情况需要考虑
          if not left_node and not right_node:
              return True
          elif not left_node and right_node:
              return False
          elif left_node and  not right_node:
              return False
          elif left_node.val != right_node.val:
              return False
          # 3.确定单层递归逻辑
          # 说白了就是继续往下比较（这样递归才能传递下去）
          outside = self.recursion(left_node.left, right_node.right)
          inside = self.recursion(left_node.right, right_node.left)
          return outside and inside
      
          # 之前错误写法
          # 说明对递归的返回值没有真正理解，这是两颗逐步变深的树，指导最后回溯告诉你，其左侧与也测是否对称（bool）
          # 只有左右侧都对称，才说明两个树镜像对称
          self.recursion(left_node.left, right_node.right)
          self.recursion(left_node.right, right_node.left)
          return True
          
  ```

  


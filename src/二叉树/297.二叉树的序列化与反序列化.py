# 题目：请设计一个算法来实现二叉树的序列化与反序列化。保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构

# 思路：序列化就是把结构化数据压成一维数据（字符串），说白了就是遍历；反序列化就是根据字符串恢复树结构。
# 105. 106.至少要得到前、中、后序遍历中的两种互相配合才能还原二叉树，那是因为前文的遍历结果没有记录空指针的信息。
# 这里的 node 列表包含了空指针的信息，所以只使用 node 列表就可以还原二叉树。


# 解法一：前序遍历
class Codec:
    # 序列化过程就是前序遍历
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                res.append('N')
                return 
              
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ','.join(res)
    # 反序列化过程 前序递归的逆过程
    # 反序列化过程也是一样，先确定根节点 root，然后遵循前序遍历的规则，递归生成左右子树即可：
    def deserialize(self, data):
        data = data.split(',')
        i = 0
        def dfs(data):
            nonlocal i
            if data[i] == 'N':
                i += 1
                return None
            node = TreeNode(int(data[i]))
            i += 1
            node.left = dfs(data)
            node.right = dfs(data)
            return node
        return dfs(data)
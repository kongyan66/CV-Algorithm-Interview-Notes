class TreeNode():
    def __init__(self, value = 0):
        self.val = value
        self.left = None
        self.right = None
# 有层序遍历构建二叉树
def bulidtree(nodeList):
    nodeList = [TreeNode(node) for node in nodeList]
    # 计算有几个节点有子节点
    parentNum = len(nodeList) // 2 - 1
    for i in range(parentNum + 1):
        leftIndex = 2 * i + 1
        rightIndex = 2 * i + 2
        nodeList[i].left = nodeList[leftIndex]
        # 判断是否有右结点， 防止数组越界
        if rightIndex < len(nodeList):
            nodeList[i].right = nodeList[rightIndex]
    return nodeList[0]

# 前序遍历
def preorder(root, res):
    if not root:
        return
    res.append(root.val)
    preorder(root.left, res)
    preorder(root.right, res)

if __name__ == '__main__':
    input, n = input().split(',')
    input = list(input)
    res = []
    tree = bulidtree(input)
    preorder(tree, res)
    print(''.join(res))


    
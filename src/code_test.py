from collections import defaultdict


def postorder(root, id):
    # 保存遍历路径，用set去重
    res = set()
    # 单层递归逻辑（不太好理解）
    for  idx in root[id]:
        res.update(postorder(root, idx))  # 更新元组，相当于extend()
    # 后续遍历
    res.add(char_map[id])  # 更新元组，相当于append()
    # 保存每个节点对应的路径
    ans[id] = res
    return res

if __name__ == '__main__':
    # 输入数据
    n = 6
    nums = [1,2, 2, 1, 4]
    chars = "ABCCAD"
    # 节点与字符的映射
    char_map = {}
    for idx,c in enumerate(chars):
        char_map[idx+1] = c

    # 这一步转换很精妙呀，用字典作记录一棵树，key为父节点，value为子节点， 通过nums的值和index+2分别找出
    trees = defaultdict(list)
    for idx, v in enumerate(nums):
        trees[v].append(idx+2)

    ans = defaultdict(set)

    # 字典树的后续遍历
    postorder(trees, 1)

    # 转换为最终结果
    ans = [str(len(ans[n+1])) for n in range(n)]
    print(' '.join(ans))


   
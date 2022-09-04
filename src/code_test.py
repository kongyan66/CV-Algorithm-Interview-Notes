# from collections import defaultdict
# nn = 6
# nums = [1,2, 2, 1, 4]
# chars = "ABCCAD"
# # print(n)
# # print(nums)
# # print(chars)

# cdts = {}
# for idx,c in enumerate(chars):
#    cdts[idx+1] = c

# trees = defaultdict(list)
# for idx,n in enumerate(nums):
#     trees[n].append(idx+2)

# print(trees)

# ans = defaultdict(set)

# def postorder(root, nd):
#     res = set()
#     for n in root[nd]:
#         res.update(postorder(root, n))
#     res.add(cdts[nd])
#     ans[nd] = res
#     return res

# postorder(trees, 1)

# # print(ans)

# ans = [str(len(ans[n+1])) for n in range(nn)]
# print(' '.join(ans))

sum = 0
res = []
sum_ = []

def test(sum):
    x = int(input())
    res.append(x)
    if x == 0:
        sum = 0 
    else:
        test(sum)
        sum += x

    sum_.append(sum)

    

if __name__ == '__main__':
    
    test(sum)
    print(res)
    print(sum_)
   
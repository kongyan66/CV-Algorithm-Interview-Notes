from collections import defaultdict
def finOddNum(arr):
    dictNum = defaultdict(int)
    for num in arr:
        dictNum[num] += 1
    for key, val in dictNum.items():
        if val % 2 == 1:
            return key

if __name__ == '__main__':
    arr = [1, 2, 1, 5, 7, 3, 4, 2, 3, 4, 3, 5, 7, 8, 8]
    ans = finOddNum(arr)
    print(ans)
n = int(input())
arr = list(map(int, input().split()))
sum = 0
def findmid(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    elif n % 2 == 0:
        return min(arr[n // 2 - 1], arr[n // 2])
    else:
        return arr[n // 2]
for i in range(n):
    for j in range(i, n):
        tem = arr[i:j+1]
        tem.sort()
        mid = findmid(tem)
        sum += mid
print(sum)

n = 2
map = ['a']
for i in range(25):
    map.append(chr(ord(map[-1]) + 1))

path = []
sum = 0

def dfs(arr):
    global sum
    if len(path) == n:
        weight = findweight(path)
        sum += weight
        return 
    
    for i in range(len(map)):
        path.append(map[i])
        dfs(arr)
        path.pop()

def findweight(path):
    weight = 0
    length = len(path)
    for i in range(0, length - 1):
        if path[i] != path[i+1]:
            weight += 1
    return weight
            

if __name__ == '__main__':
    dfs(map)
    print(sum)


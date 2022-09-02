str_map = {'0':0, 'y':1, 'e':2, 'a':3, 's':4}
nums_map = {v: k for k, v in str_map.items()}

def ten2five(n, x):
    b = []
    ans = ''
    while True:
        s = n // x # 求商
        y = n % x  # 求余
        b.append(y)
        if s == 0:
            break
        n = s
    b.reverse()
    for num in b:
        ans += nums_map[num]
    return ans

def five2ten(s, x):
    b = []
    ans = 0
    for i in range(len(s)):
        b.append(str_map[s[i]])
    b.reverse()
    for i in range(len(b)):
        ans += b[i] * x**i
    return ans

if __name__ == '__main__':  
    input = 3958
    if isinstance(input, int):
        ans = ten2five(input, 5)
        print(ans)
    else:
        ans = five2ten(input, 5)
        print(ans)












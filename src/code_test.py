def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    p, q, r = 1, 2, 1
    for i in range(3, n+1):
        p, q = q, r
        r = p + q
    return r
print(climbStairs(4))
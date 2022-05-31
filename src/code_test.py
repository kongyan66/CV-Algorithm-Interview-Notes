def strStr(haystack, needle):
    a = len(needle)
    b = len(haystack)
    if a == 0:
        return 0
    next = getnext(a, needle)
    p = -1
    for j in range(b):
        while p >= 0 and needle[p + 1] != haystack[j]:
            p = next[p]
        if needle[p + 1] == haystack[j]:
            p += 1
        if p == a - 1:
            return j - a + 1
    return -1


def getnext(a, needle):
    next = ['' for i in range(a)]
    k = -1
    next[0] = k
    for i in range(1, len(needle)):
        while k > -1 and needle[k + 1] != needle[i]:
            k = next[k]
        if needle[k + 1] == needle[i]:
            k += 1
        next[i] = k
    return next


haystack ="hello"
needle ="ll"
l = strStr(haystack, needle)
print(l)


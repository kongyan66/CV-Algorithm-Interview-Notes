def t():
    a = 2
    def tt():
        nonlocal a
        print(a)
        a += 2
        print(a)
    tt()
    print(a)
    print(a+2)
t()

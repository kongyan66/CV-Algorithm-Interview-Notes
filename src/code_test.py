def outer_fun():
    a = 1
    def fun():
        global  a # a为全局变量，与上面等于1的 a 没有关系
        a = 3 # 定义全局变量
        print(a) # 输出3
        a = 2
    fun()
    print(a) #输出1，局部变量
outer_fun()
print(a) # 输出2，全局变量


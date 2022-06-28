## 一、数据结构

### Motivation

知其用，亦知其原理



### List的底层实现

List和dict是python最常用的数据结构，其底层是CPython用C实现的。

**1）首先我们得知道[数据在内存中是如何存储的](https://www.cnblogs.com/yifeixu/p/8893823.html), 这里有两种情况：**

1.同类型数据集合如何存储  

知道头部地址，间隔一样，查找就按偏移量找

![1190058-20180420213011373-1950870200](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/1190058-20180420213011373-1950870200.png)

2.不同类型数据集合如何存储

由于类型不同，那么每个元素的内存大小不同（int 4字节，string 8字节），那么就不是等间隔了，但我们可以保存每个元素的头地址，指向位置架构就和上面一样了，这样就又可以按地址的偏移量去查找。

![img](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/1190058-20180420214515866-561856525.png)

下面看一段代码反应了list 保存不同类型数据内存特点：

[getsizeof的使用 | csdn](https://blog.csdn.net/qm5132/article/details/100557950)

```python
'''
python3.6, 64位系统(8字节）：
int28字节 float24字节 string50字节
空list64字节 dict240字节 tuple48字节 site224字节
一个指针 8字节
'''
import sys 
a = 1
list = [[], [1], ['1'], [1, 2], ['1', '2']]
for lst in list:
    print(sys.getsizeof(lst), end=' ')
print(sys.getsizeof(list))
# 输出
# 64 72 72 80 80 104
# 64 + 8*5 = 104 说明list保存的是指针而不是实际的值
```



**2）List初始化、append、insert、pop对应的[C实现](https://www.jianshu.com/p/J4U6rR)**

这块由于语言不熟悉看的不是很懂, 看着也不像c的实现

C中的结构体来实现LIst， `ob_item`是用来保存元素的指针数组，allocated是`ob_item`预先分配的内存总容量

```c
typedef struct {
    PyObject_VAR_HEAD
    PyObject **ob_item;
    Py_ssize_t allocated;
} PyListObject;
```

List初始化：

```c
arguments: size of the list = 0
returns: list object = []
PyListNew:
    nbytes = size * size of global Python object = 0
    allocate new list object
    allocate list of pointers (ob_item) of size nbytes = 0
    clear ob_item
    set list's allocated var to 0 = 0 slots
    return list object 
```



​    
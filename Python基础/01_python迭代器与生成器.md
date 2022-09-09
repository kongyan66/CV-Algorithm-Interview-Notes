## 问题

迭代器与生成器是Python最有用语言特性之一，可以说我们每次写python都用上了，也是面试高频问题，所以今天就来了解下吧！

## 迭代器(iterator)

### 定义

迭代，很简单，就是重复一个操作多次嘛。迭代器(Iterator)是一个对象，它的工作是遍历并选择序列中的对象，它提供了一种访问一个容器(container)对象中的各个元素，而又不必暴露该对象内部细节的方法。通过迭代器，开发人员不需要了解容器底层的结构，就可以实现对容器的遍历。

在python中，没有内置迭代器类型的对象，但是可以通过内置函数iter将str,tuple,list,dict,set等类型转换成一个迭代器对象。

### 可迭代对象与迭代器

#### 可迭代对象

我们每次使用 `for i in Iterable时就已经在用迭代器了，例如基本数据类型int、bool、str，还有容器类型list、tuple、dict、set。这些类型当中，有些是可迭代的，有些不可迭代，怎么判断呢？

```python 
from collections import Iterable
>>> isinstance(123, Iterable)
False
>>> isinstance([], Iterable)
True
```

可知`str,tuple,list,dict,set`是可一个可迭代对象，及可以用for语句遍历，至于为啥可以，笔者猜测是这些数据结构(对象)，支持__iter__()这个方法，怎么让一个对象可迭代呢？毕竟，很多时候，我们需要用到的对象不止Python内置的这些数据类型，还有自定义的数据类型。答案就是实现**__iter__()方法，**   **只要一个对象定义了`__iter__()`方法，那么它就是可迭代对象**.

``` python
from collections.abc import Iterable
class A():
    def __iter__(self):
        pass
print('A()是可迭代对象吗：',isinstance(A(),Iterable))
>>> A()是可迭代对象吗： True
```

#### 迭代器

迭代器是对可迭代对象的改造升级，上面说过，一个对象定义了`__iter__()`方法，那么它就是可迭代对象，进一步地，**如果一个对象同时实现了`__iter__()和__next()__()`方法，那么它就是迭代器。**

```pyhon
from collections.abc import Iterable
from collections.abc import Iterator
class B():
    def __iter__(self):
        pass
    def __next__(self):
        pass
print('B()是可迭代对象吗：',isinstance(B(), Iterable))
print('B()是迭代器吗：',isinstance(B(), Iterator))
>>>B()是可迭代对象吗： True
>>>B()是迭代器吗： True

>>> isinstance([], Iterator)
False
```

可见，**迭代器一定是可迭代对象，但可迭代对象不一定是迭代器。**

### for循环的本质

说到__iter__()和__next__()方法，就很有必要介绍一下iter()和next()方法了。

1）`iter()与__iter__()`

`__iter__()`的作用是返回一个迭代器，虽然上面说过，只要实现了`__iter__()`方法就是可迭代对象，但是，没有实现功能（返回迭代器）总归是不够的。`iter()`是Python提供的一个内置方法, 作用是来调用`__iter__()`方法。

2）`next()与__next__()`

`__next__()`的作用是返回遍历过程中的下一个元素，如果没有下一个元素则主动抛出`StopIteration`异常。而`next()`就是Python提供的一个用于调用`__next__()`方法的内置方法。

下面，我们通过next()方法来遍历一个list：

```python
>>> list_1 = [1, 2, 3]
>>> next(list_1)
Traceback (most recent call last):
File "<pyshell#19>", line 1, in <module>
next(list_1)
TypeError: 'list' object is not an iterator
>>> list_2 = iter(list_1)  # 先调用iter()才能返回一个迭代器
>>> next(list_2)
1
>>> next(list_2)
2
>>> next(list_2)
3
>>> next(list_2)
Traceback (most recent call last):
File "<pyshell#24>", line 1, in <module>
next(list_2)
StopIteration
```

**通过for循环对一个可迭代对象进行迭代时，for循环内部机制会自动通过调用iter()方法执行可迭代对象内部定义的__iter__()方法来获取一个迭代器，然后一次又一次得迭代过程中通过调用next()方法执行迭代器内部定义的__next__()方法获取下一个元素，当没有下一个元素时，for循环自动捕获并处理StopIteration异常。**

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20220908233501198.png" alt="image-20220908233501198" style="zoom:67%;" />

### 实例

以[斐波那契数列](https://www.zhihu.com/search?q=斐波那契数列&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A213544776})为例来实现一个迭代器：

```python
class FIB:
    def __init__(self, n):
        self.pre = 0
        self.cur = 1
        self.n = n

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n > 0:
            value = self.cur
            self.cur += self.pre
            self.pre = value
            self.n -= 1
            return value
        else:
            raise StopIteration

f = FIB(10)
print([i for i in f])
```



## 生成器



## 二者关系

![preview](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-95b4076d30e55da078045cdade28cea3_r.jpg)

## 参考

[为什么for循环能遍历list](https://www.cnblogs.com/chenhuabin/p/11288797.html#_label1)

[如何更好地理解Python迭代器和生成器？](https://www.zhihu.com/question/20829330)

[Iterables vs. Iterators vs. Generators](https://nvie.com/posts/iterators-vs-generators/)
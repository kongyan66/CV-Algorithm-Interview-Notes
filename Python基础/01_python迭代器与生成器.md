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



### 实例

以[斐波那契数列](https://www.zhihu.com/search?q=斐波那契数列&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A213544776})为例来实现一个迭代器：

```python

```







## 参考

[为什么for循环能遍历list](https://www.cnblogs.com/chenhuabin/p/11288797.html#_label1)
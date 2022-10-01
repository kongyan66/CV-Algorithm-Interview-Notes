## 问题

迭代器与生成器是Python最有用语言特性之一，可以说我们每次写python都用上了，也是面试高频问题，所以今天就来整透彻了！

## 迭代器(iterator)

### 定义

迭代，很简单，就是重复一个操作多次嘛。迭代器(Iterator)是一个对象，它的工作是遍历并选择序列中的对象，它提供了一种访问一个容器(container)对象中的各个元素，而又不必暴露该对象内部细节的方法。通过迭代器，开发人员不需要了解容器底层的结构，就可以实现对容器的遍历。

在python中，没有内置迭代器类型的对象，但是可以通过内置函数iter将str,tuple,list,dict,set等类型转换成一个迭代器对象。

### 可迭代对象与迭代器

#### 可迭代对象

我们每次使用 `for i in Iterable`时就已经在用迭代器了，但基本数据类型int、bool、str，还有容器类型list、tuple、dict、set。这些类型当中，有些是可迭代的，有些不可迭代，怎么判断呢？

```python 
from collections import Iterable
>>> isinstance(123, Iterable)  # 判断类型
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

### 定义

在 Python 中还有一种函数，用关键字 yield 来返回值，这种函数叫生成器函数，函数被调用时会返回一个生成器对象，**生成器本质上还是一个特殊的迭代器**，也是用在迭代操作中，因此它有和迭代器一样的特性，唯一的区别在于实现方式上不一样，**后者更加简洁**。

### 迭代器与生成器

那为何用生成器做迭代器就这么方便呢？在调用该生成器函数时，Python会自动在其内部添加__iter__()方法和__next__()方法。把生成器传给 next() 函数时， 生成器函数会向前继续执行， 执行到函数定义体中的下一个 yield 语句时， 返回产出的值， 并在函数定义体的当前位置暂停， 下一次通过next()方法执行生成器时，又从上一次暂停位置继续向下……，最终， 函数内的所有yield都执行完，如果继续通过yield调用生成器， 则会抛出StopIteration 异常——这一点与迭代器协议一致。

可以看到，生成器的执行机制与迭代器是极其相似的，生成器本就是迭代器，只不过，有些特殊。那么，生成器特殊在哪呢？或者说，有了迭代器，为什么还要用生成器？**生成器采用的是一种惰性计算机制**，一次调用也只会产生一个值，它不会将所有的值一次性返回给你，你需要一个那就调用一次next()方法取一个值，这样做的好处是如果元素有很多（数以亿计甚至更多），如果用列表一次性返回所有元素，那么会消耗很大内存，如果我们只是想要对所有元素依次一个一个取出来处理，那么，使用生成器就正好，一次返回一个，**并不会占用太大内存。**

### 实现方式

**生成器函数**

说白了就是采用`yield`的函数就是一个生成器

```python
>>> from collections.abc import Iterable
>>> from collections.abc import Iterator
>>> def func(n):
...     yield n*2
>>> g = gen(2)
>>> isinstance(g, Iterable)
True
>>> isinstance(g, Iterator)
True
>>> next(g)
>>> 4
```

**生成器表达式**

生成器表达式与列表推导式长的非常像，但是它俩返回的对象不一样，前者返回生成器对象，后者返回列表对象。

```
#生成器表达式
>>> g = [x*2 for x in range(10)]
>>> type(g)
<type 'generator'>
# 列表表达式
>>> l = [x*2 for x in range(10)]
>>> type(l)
<type 'list'>
```

### 实例

举个例子，假设我们现在要取1亿以内的所有偶数，如果用列表来实现，代码如下：

```python 
def fun_list():
    index = 1
    temp_list = []
    while index < 100000000:
        if index % 2 == 0:
            temp_list.append(index)
            print(index)
        index += 1
    return temp_list
```

上面程序会先获取所有符合要求的偶数，然后一次性返回。如果你运行了代码，你就会发现两个问题——运行时间很长、消耗很多内存。

有时候，我们并不一定需要一次性获得所有的对象，需要一个使用一个就可以，这样的话，可以用生成器来实现：

```pyhon
>>> def fun_gen():
    　　index = 1
    　　while index < 100000000:
      　　  if index % 2 == 0:
      　　      yield index
      　　  index += 1

        
>>> fun_gen()
<generator object fun_gen at 0x00000222DC2F4360>
>>> g = fun_gen()
>>> next(g)
2
>>> next(g)
4
>>> next(g)
6
```





## 二者关系

![preview](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-95b4076d30e55da078045cdade28cea3_r.jpg)

## 参考

[为什么for循环能遍历list](https://www.cnblogs.com/chenhuabin/p/11288797.html#_label1)

[如何更好地理解Python迭代器和生成器？](https://www.zhihu.com/question/20829330)

[Iterables vs. Iterators vs. Generators](https://nvie.com/posts/iterators-vs-generators/)
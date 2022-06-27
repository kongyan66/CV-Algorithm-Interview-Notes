## 一、数据结构

### Motivation

知其用，亦知其原理



### List的底层实现

List和dict是python最常用的数据结构，其底层是CPython用C实现的。

1）首先我们得知道**[数据在内存中是如何存储的](https://www.cnblogs.com/yifeixu/p/8893823.html)**, 这里有两种情况：

1.同类型数据集合如何存储  

![1190058-20180420213011373-1950870200](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/1190058-20180420213011373-1950870200.png)

2.不同类型数据
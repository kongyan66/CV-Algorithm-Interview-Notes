## 问题

一直都在用，今天就总结下！

## 概括

Python 在 heap 中分配的对象分成两类：可变对象和不可变对象。所谓可变对象是指，对象的内容是可变的，例如 list。而不可变的对象则相反，表示其内容不可变。

> ```
> 不可变对象 ：int，string，float，tuple   -- 可理解为C中，该参数为值传递
> 可变对象   ：list，dictionary           -- 可理解为C中，该参数为指针传递
> ```

## 不可变对象

由于 Python 中的变量存放的是**对象引用**，所以对于不可变对象而言，尽管对象本身不可变，但变量的对象引用是可变的。运用这样的机制，有时候会让人产生糊涂，似乎可变对象变化了。如下面的代码：

```python
i = 73  
i += 2
```

![image-20221002171922893](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221002171922893.png)

从上面得知，**不可变的对象的特征没有变，****依然是不可变对象，变的只是创建了新对象，改变了变量的对象引用**。

上面说到了python变量存放的是变量引用，以下代码能说明这点：

```python
#因为258是int对象，是不可变对象的。所以下面3个id的值都是一样的，最后一句的结果也是为True  
print(id(258))  
a = 258  
print(id(a))  
b = 258  
print(id(b))  
print(a is b)  

>>>
140386942355760
140386942355760
140386942355760
True
```

## 可变对象

其对象的内容是可以变化的。当对象的内容发生变化时，变量的对象引用是不会变化的。如下面的例子:

```python
m = [5,9]  
m += [6] 
```

![image-20221002192023410](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221002192023410.png)

## 参考

[Python可变对象和不可变对象](https://www.runoob.com/note/46684)
## 问题

在数据处理时候，常常会有将python对象与JSON对象相互转换的需求，比如数据标签的制作。

## 什么是JSON 

JSON 指的是 JavaScript 对象表示法（**J**ava**S**cript **O**bject **N**otation），是轻量级的文本数据交换格式，都用于接收 web 服务端的数据。说白了就是一种存储数据的结构。

## 什么是python对象与json对象

所谓python对象就是python的数据结构, 如字符串、字典等，本质上还是一个class, 所以通常统称为python对象；同理，json对象只是json数据保存的格式。以下是json类型转换到python的类型对照表：

**python转json:**

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221021215659313.png" alt="image-20221021215659313" style="zoom:80%;" />

**json转python：**

<img src="C:\Users\10428\AppData\Roaming\Typora\typora-user-images\image-20221021215440574.png" alt="image-20221021215440574" style="zoom: 80%;" />

可见json中有`object` `array`	`string` `number` 等数据类型，这与python的 叫法可能有点不同，但在形式上基本一致，比如json中的`object`与python的`dict`形式完全一致。

## python对象与json对象互换

Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含四个常用的函数：

| 函数                | 描述                                     |
| :------------------ | :--------------------------------------- |
| json.dumps          | 将 Python 对象编码成 JSON 字符串         |
| json.loads          | 将已编码的 JSON 字符串解码为 Python 对象 |
| json.dump(dict, fp) | 把dict转换成str类型存到fp指向的文件里    |
| json.load(fp)       | 把fp指向的文件里的内容读取出来           |

下面演示如何将一个Python数据结构转换为JSON：

```python
import json
data = {
    'name':xiaming,
    'age':25,
    'height':178
}
json_str = json.dumps(data)  # <class 'str'>
```

下面演示如何将一个JSON编码的字符串转换回一个Python数据结构：

```python
data = json.loads(json_str) # <class 'dict'>
```

如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。例如：

```python
# 写入
with open('data.json', 'r') as f:
    json.dump(data, f)
# 读出
with open('data.json', 'w') as f:
    data = json.load(f)
```



## 参考

[**python中json.dump() 和 json.dumps() 有那些区别？**](https://blog.51cto.com/u_14246112/3141416)

[python json | 菜鸟教程](https://www.runoob.com/python/python-json.html)
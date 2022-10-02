## python 模块导入

### 问题

工程整体跑没事，单独调试某一个模块时就总会有一些自己写的代码无法导入（第三方包不存在该情况），无论是相对还是绝对导入都没解决，下面就说明下造成该问题的原因。

### 什么是脚本，什么是模块？

![img](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/20191022153358921.png) 

### 绝对导入

![img](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/201910221543249.png) 

### 相对导入

![img](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/20191022155159139.png) 

**脚本不能包含包含相对导入**

![img](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/20191022155315967.png) 

![在这里插入图片描述](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/20191022155559258.png) 

**解决办法**

![img](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/20191022155832217.png) 

### 参考

[python包导入细节](https://blog.csdn.net/suiyueruge1314/article/details/102683546)


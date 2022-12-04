# 第一章 计算机系统漫游

## 代码的的本质

就是字符串通过ASCII码翻译成单字节大小的整数值。

## 程序的编译过程

汇编语言为不同高级语言的不同编译器提供了通用的输出语言。

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221204173228860.png" alt="image-20221204173228860" style="zoom:50%;" />

## 程序执行过程

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221204192749917.png" alt="image-20221204192749917" style="zoom: 50%;" />

## 操作系统管理硬件

操作系统两个基本功能：

- 防止硬件被失控应用程序所滥用
- 向应用提供简单一致的接口来控制低级硬件设备

操作系统通过进程、虚拟存储器、文件来实现以上功能。其中进程是对处理器、主存、I/O设备的抽象；虚拟存储器是对主存和磁盘I/O设备的抽象；文件是对I/O设备的抽象。

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221204193416034.png" alt="image-20221204193416034" style="zoom:50%;" />

### 进程

**进程是操作系统对一个正在运行的程序的一种抽象**。并发运行是说一个进程的指令和另一个进程的指令交错进行。无论在单核还是多核系统中，一个CPU看上去好像是在并发执行多个进程，其实是在进程间的切换来实现的（任何时刻，单处理系统只能执行一个进程的代码）。操作系统实现这种交错执行的机制称为**上下文切换**。

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221204194138081.png" alt="image-20221204194138081" style="zoom:50%;" />

### 线程

一个进程也可以由多个称为线程的执行单组成，每隔线程都运行在进程的上下文中，并共享同样的代码和全局函数。

由于网络服务器对并行处理的需求，多线程就很重要，因为多线程之间比多进程之间更容易共享数据，也更高效；当多处理器可用时，多线程也是使得程序运行更快的方法。

### 虚拟存储器

虚拟存储器是一个抽象概念，它为每一个进程提供了一个假象，即每一个进程都在单独占用使用主存，每一个进程看到的是一致的存储器，称为虚拟存储地址。

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221204195622693.png" alt="image-20221204195622693" style="zoom:50%;" />

### 并发与并行

并发指一个同时具有多个活动的系统；并行只用并发使一个系统运行的更快。并行可以在计算机系统多个抽象层次上运行，以下是由高到低的顺序的并行：

- 线程级并发
- 指令级并行
- 单指令、多数据并行

## 小结

计算机系统是由硬件和系统软件组成，它们共同协作以运行程序。程序被其他程序翻译成不同的形式，开始时是ASCII文本，然后编译器和链接器翻译成二进制可执行文件。



# 第二章 信息的表示与处理



# 参考

[**课程主页**](http://www.cs.cmu.edu/afs/cs/academic/class/15213-f15/www/schedule.html)

**视频：**

- [bilibi-CSAPP-深入理解计算机系统](https://www.bilibili.com/video/BV1tV411U7N3/?spm_id_from=pageDriver&vd_source=9fd24d506f93429d3b579d92063785a2)
- [blibli-15-213 CSAPP 深入理解计算机系统(CMU)](https://www.bilibili.com/video/av31289365/?vd_source=9fd24d506f93429d3b579d92063785a2)

**仓库**：

- [vonzhou/CSAPP](https://github.com/vonzhou/CSAPP)


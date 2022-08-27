# YOLOv1-v5 系列详解

## YOLOv1

核心思想：分类器输出一个one-hot vector，那我把它换成**(x,y,w,h,c)**，c表示confidence置信度，把问题转化成一个回归问题，直接回归出Bounding Box的位置不就好了吗？**本质上都是矩阵映射到矩阵，只是代表的意义不一样而已。**

### 数据维度

我们把图像划分成7*7个区域(grid), 用二个(c, x, y, w, h, one-hot)，去负责image该区域的大小目标的预测, 其实每一个grid都可以看做一个检测器，这样模型输出维度就为`7 * 7 * (2 * 5 + classes)`

### 模型结构

24 卷积层+2 全连接层 

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-3af308f7096bda4c621c077302b90533_r.jpg" alt="preview" style="zoom:80%;" />

### 损失设计

loss设计的前提是标签先确定好，这里面**c的真值该怎么设置呢**？如果一个目标的中心落入了一个grid,那么当前grid的c值就为1，也就说当前grid负责该目标的预测。

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-f81c565d41b681263689626331325ac3_r.jpg" alt="preview" style="zoom:80%;" />

前2行计算前景的geo_loss，即位置损失。

第3行计算前景的confidence_loss，统称置信度损失。

第4行计算背景的confidence_loss。

第5行计算分类损失class_loss，即分类损失。



### 优缺点

#### 已解决

- **多目标、多类别检测**

  每一个网格去预测目标的位置(x,y,w,h)、置信度(c)、类别(class)，输出维度为 `5 * box数量 + classes`

- **采用NMS进行多框过滤**

  分别对用类目标的置信度进行排序，取置信度最大的框作为目标框，然后与其他所有框做IOU计算，大于某阈值的剔除(说明与目标框很接近，一山不容二虎)，然后在选取第二个目标框，同上操作，直到没有剩下的框了(所有目标框都找出来了，没有重复框了)

- **大小目标检测**

  对于每个区域，我们用2个五元组(c,x,y,w,h)，一个负责回归大目标，一个负责回归小目标，

#### 未解决

- **同一个grid只能预测一个目标**

  两个目标中心都落到一个网格中

- **样本不均衡的问题**

  没有计算背景的geo_loss，只计算了前景的geo_loss，这个问题YOLO v1回避了，依然存在。



我们认为，**检测模型=特征提取器+检测头**

在YOLO v1的模型中检测头就是最后的2个全连接层(Linear in PyTorch)，它们是参数量最大的2个层，也是最值得改进的2个层。后面的YOLO模型都对这里进行改进：

## Yolov2

我们认为，**检测模型 = 特征提取器 + 检测头**

在YOLO v1的模型中检测头就是最后的2个全连接层(Linear in PyTorch)，它们是参数量最大的2个层，也是最值得改进的2个层。后面的YOLO模型主要就是对**特征提取**(backbone + neck) 和**检测头**的改进。

### backbone



### head

YOLO v1虽然快，但是预测的框不准确，很多目标找不到：

- **预测的框不准确：准确度不足。**
- **很多目标找不到：recall不足。**

#### 问题一：如何提高准确度

**同时代别人怎么做的呢？**

同时代的检测器有R-CNN，人家预测的是偏移量。什么是偏移量？

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-4883b178ed0e2bb95f1d504dc6bed6a7_r.jpg" alt="preview" style="zoom:67%;" />

之前YOLO v1直接预测x,y,w,h，范围比较大，现在我们想预测一个稍微小一点的值，来增加准确度。不得不先介绍2个新概念：**基于grid的偏移量和基于anchor的偏移量**。什么意思呢？

- **基于anchor的偏移量**的意思是，anchor的位置是固定的，**偏移量=目标位置-anchor的位置**。

- **基于grid的偏移量**的意思是，grid的位置是固定的，**偏移量=目标位置-grid的位置**。









#### 问题二：如何提高recall



## 参考

[你一定从未看过如此通俗易懂的YOLO系列(从v1到v5)模型解读(上)](https://zhuanlan.zhihu.com/p/183261974)

[你一定从未看过如此通俗易懂的YOLO系列(从v1到v5)模型解读 (中)](https://zhuanlan.zhihu.com/p/183781646)
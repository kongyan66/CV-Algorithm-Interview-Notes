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

## YOLO v2

我们认为，**检测模型 = 特征提取器 + 检测头**

在YOLO v1的模型中检测头就是最后的2个全连接层(Linear in PyTorch)，它们是参数量最大的2个层，也是最值得改进的2个层。后面的YOLO模型主要就是对**特征提取**(backbone + neck) 和**检测头**的改进。

### backbone



### head

YOLO v1虽然快，但是预测的框不准确，很多目标找不到：

- **预测的框不准确：准确度不足。**
- **很多目标找不到：recall不足。**

#### 问题一：如何提高准确度

YOLO v2改预测偏移量而不是直接去预测 (x,y,w,h)， 人家预测的是偏移量。另一个重要的原因是：直接预测位置会导致神经网络在一开始训练时不稳定，使用偏移量会使得训练过程更加稳定，性能指标提升了5%左右。

#### 问题二：如何提高recall

**YOLO v1一次能检测多少个目标吗**？答案是**49个目标**，98个框，并且2个框对应一个类别。可以是大目标也可以是小目标。因为输出的尺寸是：[N, 7, 7, 30]。式中N为图片数量，7,7为49个区域(grid)。

$$30=2×5(c,x,y,w,h)+1×20classes$$

**YOLO v2**首先把 7×7 个区域改为 **13×13** 个区域，每个区域有**5**个anchor，且每个anchor对应着1个类别，那么，输出的尺寸就应该为：[N,13,13,125]。

$$125=5×5(c,x,y,w,h)+5×20classes$$

这里面有个bug，就是YOLO v2先对每个区域得到了5个anchor作为参考，那你就会问2个问题：

**1. 为什么要用Anchor呢？**

**一开始YOLO v1的初始训练过程很不稳定**，在YOLO v2中，作者观察了很多图片的所有Ground Truth，发现：比如车，GT都是矮胖的长方形，再比如行人，GT都是瘦高的长方形，且宽高比具有相似性。那**能不能根据这一点，从数据集中预先准备几个几率比较大的bounding box，再以它们为基准进行预测呢？**这就是Anchor的初衷。

**2. 每个区域的5个anchor是如何得到的？**

对于任意一个数据集，就比如说COCO吧(紫色的anchor)，先对训练集的GT bounding box进行聚类，聚成几类呢？作者进行了实验之后发现**5**类的**recall vs. complexity**比较好，现在聚成了**5**类，当然9类的mAP最好，预测的最全面，但是在复杂度上升很多的同时对模型的准确度提升不大，所以采用了一个比较折中的办法选取了5个聚类簇，即使用5个先验框。

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-7e157d61f41ca02634f06b0b78c71684_r.jpg" alt="preview" style="zoom: 67%;" />

所以到现在为止，有了anchor再结合预测值 tx,ty,tw,th ，就可以求出目标位置。

结论是，**anchor是从数据集中统计得到的(Faster-RCNN中的Anchor的宽高和大小是手动挑选的)。**

### Loss

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-faed5df5818795d5fc047815f0338768_r.jpg" alt="preview" style="zoom:80%;" />

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20220827213624292.png" alt="image-20220827213624292" style="zoom:80%;" />

### 小结

YOLO v2做了这么多改进，整体性能大幅度提高，但是小目标检测仍然是YOLO v2的痛。直到kaiming大神的ResNet出现，backbone可以更深了，所以darknet53诞生。

最后我们做个比较：

![preview](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-e4dce0794b6d4aa5a67133633baed6b4_r.jpg)



## YOLO v3

### backbone改进

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-085b6d95dc53894e5de4fe95d2249b06_r.jpg" alt="preview" style="zoom: 67%;" />

###  head改进

之前在说小目标检测仍然是YOLO v2的痛，YOLO v3是如何改进的呢？如下图所示。

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-4cf1b6f6afec393122305ca2bb2725a4_r.jpg" alt="preview" style="zoom: 50%;" />

我们知道，YOLO v2的检测头已经由YOLO v1的 7×7 变为 13×13了，我们看YOLO v3检测头分叉了，分成了3部分：

- 13*13*3*(4+1+80)
- 26*26*3*(4+1+80)
- 52*52*3*(4+1+80)

这样预测的框更多更全面了，并且分级了。**anchor和YOLO v2一样，依然是从数据集中统计得到的。**

我们发现3个分支分别为**32倍下采样，16倍下采样，8倍下采样**，分别取预测**大，中，小目标**。为什么这样子安排呢？

因为**32倍下采样**每个点感受野更大，所以去预测**大目标，8倍下采样**每个点感受野最小，所以去预测**小目标。专人专事。**

又有人会问，你现在是3个分支，我改成5个，6个分支会不会更好？理论上会，但还是那句话，作者遵循recall vs. complexity的trade off。

### loss改进

yolov3 loss分3部分组成：定位损失+置信度损失+分类损失，本质就是算各个grid(一个grid看做一个小检测器)的损失和。
第1行代表geo_loss，S代表13,26,52，就是grid是几乘几的。B=5。
第2行代表confidence_loss，和YOLO v2一模一样。
第3行代表class_loss，和YOLO v2的区别是改成了交叉熵。

![preview](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-1714579e2a7f9ca88335bdaeae9e1c4f_r.jpg)

**分类损失**

YOLO v3使用多标签分类，用多个独立的logistic分类器代替softmax函数，以计算输入属于特定标签的可能性。在计算分类损失进行训练时，YOLO v3对每个标签使用二元交叉熵损失。

**正负样本确定**

如果某个anchor与 GT 目标IOU 值最大，则则相应的目标性得分应为 1

对于重叠大于等于0.5的其他先验框(anchor)，忽略，不算损失。

对于重叠小于0.5的其他先验框(anchor)，负样本。

> 每个 GT 目标**仅与一个先验边界框相关联**。 如果没有分配先验边界框，则不会导致**分类和定位损失，只会有目标性的置信度损失。**



## YOLO v4

### backbone 改进



### head改进

**1. Using multi-anchors for single ground truth**

之前的YOLO v3是1个anchor负责一个GT，YOLO v4中用多个anchor去负责一个GT。方法是：对于 GTj 来说，只要 IoU(anchori,GTj)>threshold ，就让 anchori 去负责 GTj 。

这就相当于你anchor框的数量没变，但是选择的**正样本**的比例增加了，就**缓解了正负样本不均衡的问题**。

**2.Eliminate_grid sensitivity**

还记得之前的YOLO v2的这幅图吗？YOLO v2，YOLO v3都是预测4个这样的偏移量

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-63ca4ed417c5db83b18c95a42a7f60f2_r.jpg" alt="preview" style="zoom: 50%;" />

这里其实还隐藏着一个问题：

模型预测的结果是： tx,ty,tw,th ，那么最终的结果是： bx,by,bw,bh 。这个 b 按理说应该能取到一个grid里面的任意位置。但是实际上边界的位置是取不到的，因为sigmoid函数的值域是： (0,1) ，它不是 [0,1] 。所以作者提出的Eliminate_grid sensitivity的意思是：将 bx,by 的计算公式改为：

![image-20220829155335088](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20220829155335088.png)

这里的1.1就是一个示例，你也可以是1.05,1.2等等，反正要乘上一个略大于1的数，作者发现经过这样的改动以后效果会再次提升。

### loss改进

改进路线：**MSE Loss → IoU Loss→ GIoU Loss→ DIoU Loss→ CIoU Loss**

之前的YOLO v2，YOLO v3在计算geo_loss时都是用的MSE Loss，之后人们开始使用IoU Loss。

**IOU loss**

$ L_{iou} = 1 - \frac{B\cap B_{gt}}{B \cup B_{gt}}$ ，它可以反映预测检测框与真实检测框的检测效果。

但是问题也很多：不能反映两者的距离大小（重合度）。同时因为loss=0，**当GT和bounding box不挨着时，没有梯度回传，无法进行学习训练。**如下图4所示，三种情况IoU都相等，但看得出来他们的重合度是不一样的，左边的图回归的效果最好，右边的最差：

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-a52e8fc7166b29c08b80de1ead22ec79_r.jpg" alt="preview" style="zoom: 50%;" />

**GIOU loss**

**所以接下来的改进是：**

$ L_{GIOU} = 1 - IOU + \frac{C- B\cup B_{gt}}{|C|}$ , $C$ 为同时包含了预测框和真实框的最小框的面积.

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-4ccbf64fa4eefb0e321809a803f90c74_r.jpg" alt="preview" style="zoom:50%;" />

GIoU Loss可以解决上面IoU Loss对距离不敏感的问题。但是GIoU Loss存在训练过程中**发散**等问题。

**DIOU**

$ L_{DIOU} = 1 - IOU + \frac{\rho^2(b, b^{gt})}{|c^2|}$, 其中，$b$, $b^{gt}$ 分别表示预测框和真实框的中心点，且$\rho $代表计算两个中心的**欧式距离**。$c$代表是能够同时包含预测框和真实框的**最小闭包区域**的对角线距离。

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-2345aacc478cc5523d439ffcd84958ac_r.jpg" alt="preview" style="zoom:50%;" />

**DIoU loss**可以直接最小化两个目标框的距离，因此比GIoU loss收敛快得多。

**DIoU loss除了这一点之外，还有一个好处是：**

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-3db202166e0c206001ca03e191489532_r.jpg" alt="preview" style="zoom: 50%;" />

​																				IoU Loss和GIoU loss都一样时

如上图所示，此3种情况IoU Loss和GIoU loss都一样，但是DIoU Loss右图最小，中间图次之，左图最大。

**小结**：DIOU 收敛快，缓解Bbox包含GT的问题 ，**依然没有彻底解决包含的问题**，即

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-96838980b7fd4443661cf0019802ea7b_r.jpg" alt="preview" style="zoom:50%;" />

这2种情况$b$和 $b^{gt}$是重合的，DIoU loss的第3项没有区别，所以在这个意义上DIoU loss依然存在问题。

**CIOU**

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20220829172635777.png" alt="image-20220829172635777" style="zoom:67%;" />



## 参考

[你一定从未看过如此通俗易懂的YOLO系列(从v1到v5)模型解读(上)](https://zhuanlan.zhihu.com/p/183261974)

[你一定从未看过如此通俗易懂的YOLO系列(从v1到v5)模型解读 (中)](https://zhuanlan.zhihu.com/p/183781646)


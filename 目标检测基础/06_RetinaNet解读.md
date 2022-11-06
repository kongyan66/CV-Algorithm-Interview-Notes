## 问题

虽说RetinaNet与YOLO系列挺像，但在FPN和分类损失函数，还是有一些区别。

## 网络结构

![image-20221105143200965](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221105143200965.png)

整个网络分为三大部分：

1. **Backbone**: 基础特征提取，论文使用resnet

   `Retinanet` 的 `Backbone` 为 `ResNet` 网络，`ResNet` 一般从 `18` 层到 `152` 层（甚至更多）不等，主要区别在于采用的残差单元/模块不同或者堆叠残差单元/模块的数量和比例不同，论文主要使用 `ResNet50`。

2. **FPN**：多尺度特征提取

   `Neck` 模块即为 `FPN` 网络结构。FPN 模块接收 c3, c4, c5 三个特征图，输出 P2-P7 五个特征图，通道数都是 256, stride 为 (8,16,32,64,128)，**其中大 stride (特征图小)用于检测大物体，小 stride (特征图大)用于检测小物体**。P6 和 P7 目的是提供一个**大感受野强语义**的特征图，有利于大物体和超大物体检测。注意：在 RetinaNet 的 FPN 模块中只包括卷积，不包括 BN 和 ReLU。

   对于retinanet使用的FPN结构略有变化，使用更低的分辨率，使用了更多的检测头，这些改动加速了运算，总体accuracy略有提升。

   > P2未使用
   >
   > P6是在C5上使用3*3 stride-2 convolution得到
   >
   > P7 是P6通过relu之后使用3*3 stride-2 convolution 得到

   <img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221105143821643.png" alt="image-20221105143821643" style="zoom:50%;" />

​     

3. **Head**: FCN（两个子网络）：

   `YOLOv3` 的 `neck` 输出 `3` 个分支，即输出 `3` 个特征图， `head` 模块只有一个分支，由卷积层组成，该卷积层完成目标分类和位置回归的功能。总的来说，`YOLOv3` 网络的 `3` 个特征图有 `3` 个预测分支，分别预测 `3` 个框，也就是分别预测大、中、小目标。

   `Retinanet` 的 `neck` 输出 `5` 个分支，即输出 `5` 个特征图。`head` 模块包括分类和位置检测两个分支，每个分支都包括 `4` 个卷积层，但是 `head` 模块的这两个分支之间参数不共享，分类 `Head` 输出通道是 A*K，A 是类别数；检测 `head` 输出通道是 4*K, K 是 anchor 个数, 虽然每个 Head 的分类和回归分支权重不共享，但是 `5` 个输出特征图的 Head 模块权重是共享的。

## 核心问题

**解决正负样本不均衡的问题，在正常的cross entropy函数中，正样本的总损失远远小于负样本的总损失。**


一张图像中能够匹配到目标候选框（正样本）数量一般只有十几个或几十个，而没匹配到的候选 框（负样本）大概会有$10^4-10^5$(根据设定的锚框数量而定)。在这$10^4-10^5$个未匹配到的目标的候选框中大部分都是简单易分的负样本（对训练不起什么作用，loss值比较低，但人家数量多啊，这就可能淹没掉数量少正样本的loss），比如有50个正样本,10000个负样本，每个正样本贡献损失是3，每个负样本贡献的损失是0.1，正样本的总损失是$50 * 3 = 150$, 负样本的总损失是$10000 * 0.1 = 1000$，正样本对模型产生的影响远小于负样本，这样是非常不合理的。

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221105144924150.png" alt="image-20221105144924150" style="zoom: 67%;" />

### 之前的措施

1. Yolo V1的解决方案：对正样本和负样本分别计算置信度损失，使用权重控制影响
2. SSD的解决方案：使用hard negative mining，对负样本选择置信度较小的top k，然后保持正负样本比例为1：3

### Focal Loss

`Focal Loss` 是在二分类问题的交叉熵（`CE`）损失函数的基础上引入的，所以需要先学习下交叉熵损失的定义。

**Cross Entropy**

在深度学习中我们常使用交叉熵来作为分类任务中训练数据分布和模型预测结果分布间的代价函数。对于同一个离散型随机变量 x 有两个单独的概率分布 P(x) 和 Q(x) ，其交叉熵定义为(P 表示真实分布， Q 表示预测分布)：

![image-20221106094427682](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221106094427682.png)

但在实际计算中，我们通常不这样写，因为不直观。在深度学习中，以二分类问题为例，其交叉熵损失（`CE`）函数如下：

![image-20221106094506777](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221106094506777.png)

其中 p 表示当预测样本等于 1 的概率，则 1−p 表示样本等于 0 的预测概率。因为是二分类，所以样本标签 y 取值为 {1,0} (若多分类y 取值为 {1,0, 0, 0, ....})，上式可缩写至如下：

![image-20221106094558931](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221106094558931.png)

为了方便，用 pt 代表 p ， pt 定义如下：

![image-20221106094629044](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221106094629044.png)

则（3）式可写成：

![image-20221106094651575](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221106094651575.png)

前面的交叉熵损失计算都是针对单个样本的，对于**所有样本**，二分类的交叉熵损失计算如下：

![image-20221106094737172](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221106094737172.png)

其中 m 为正样本个数， n 为负样本个数， N 为样本总数， m+n=N 。当样本类别不平衡时，损失函数 L 的分布也会发生倾斜，如 m≪n 时，负样本的损失会在总损失占主导地位。又因为损失函数的倾斜，模型训练过程中也会倾向于样本多的类别，造成模型对少样本类别的性能较差。

再衍生以下，对于**所有样本**，多分类的交叉熵损失计算如下：

![image-20221106094816018](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221106094816018.png)

其中， M 表示类别数量， $y_{ic}$是符号函数，如果样本 i 的真实类别等于 c 取值 1，否则取值 0; $p_{ic}$表示样本 i 预测为类别 c 的概率。

**Balanced Cross Entropy**

对于正负样本不平衡的问题，较为普遍的做法是引入 α∈(0,1) 参数来解决，上面公式重写如下：

![image-20221106095247658](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221106095247658.png)

对于所有样本，二分类的平衡交叉熵损失函数如下：

![image-20221106095350048](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221106095350048.png)

其中 α / 1−α=n / m ，即 α 参数的值是根据正负样本分布比例来决定的。虽然 α 参数平衡了正负样本（`positive/negative examples`），但是它并不能区分难易样本，而实际上，目标检测中大量的候选目标都是易分样本。这些样本的损失很低，但是由于难易样本数量极不平衡，易分样本的数量相对来讲太多，最终主导了总的损失。

**Foacl loss**

本文的作者认为，易分样本（即，置信度高的样本）对模型的提升效果非常小，模型应该主要关注与那些难分样本（这个假设是有问题的，是 `GHM` 的主要改进对象）**本质就是让易分的样本loss值变小，让模型重点学习难区分的样本。形式上是对CE基础上加了一个衰减因子。**

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221105153001225.png" alt="image-20221105153001225" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221105153137073.png" alt="image-20221105153137073" style="zoom:67%;" />

1. $p_t$=真实的标签对应的confidence score（神经网络对真实标签的softnax输出）,正样本就是$p$， 负样本就是$1-p$.
2. 其中αt用来手动控制各个class的权重，解决了正负样本不平衡的问题
3. 而$(1−p_t)^y$, 实验中γ=2效果最好。这样了保证难分类的( $ p_{\mathrm{t}} $ 较小)的样本在损失函数中更显著，从而保证神经网络着重优化难分类的样本。

下图反应了不同$y$下，不同P参数loss的变化曲线，可见P越大，产生的loss越小，不同的$y$影响着Loss的大小，这就起到区分难易样本的作用了。

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221105153650142.png" alt="image-20221105153650142" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221105153759560.png" alt="image-20221105153759560" style="zoom:50%;" />

最后，我们用实例体现下Focal loss是如何平衡难易样本的。下图中蓝色和红色为易区分样本，绿色为难区分样本，相比于`CE loss`产生的loss更小，对于后者，产生loss都差不多，这样模型就能更聚焦于难样本的学习。

![image-20221105153924256](https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20221105153924256.png)



## 参考

[一阶段目标检测器-RetinaNet网络详解](https://zhuanlan.zhihu.com/p/410436667) 非常全面

[Retina Net 与Focal Loss](https://zhuanlan.zhihu.com/p/258974272)

[RetinaNet网络结构详解](https://www.bilibili.com/video/BV1Q54y1L7sM/?spm_id_from=333.999.0.0&vd_source=9fd24d506f93429d3b579d92063785a2) 视频讲解
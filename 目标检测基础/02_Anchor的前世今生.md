# Anchor的一生

anchor的机制本质上，就是一堆变scale和ratio的滑动窗口，只不过通过CNN的Dense Map Prediction的方式整个嵌入到一个end2end的框架里面了。

## **Anchor缘起**

YOLO v1的初始训练过程很不稳定，在YOLO v2中，作者观察了很多图片的所有Ground Truth，发现：比如车，GT都是矮胖的长方形，再比如行人，GT都是瘦高的长方形，**且宽高比具有相似性**。那能不能根据这一点，从数据集中预先准备几个几率比较大的bounding box，再以它们为基准进行预测呢？**这就是Anchor的初衷，它将预测最终检测框作为唯一的使命！**

## Anchor的诞生

那么，anchor到底是什么呢, 怎么来的？如果我们用一句话概括——**就是在图像上预设好的不同大小，不同长宽比的参照框。**（其实非常类似于上面的滑窗法所设置的窗口大小）。

下图来自《动手学深度学习》中的例子，假设一个256x256大小的图片，经过64、128和256倍下采样，会产生4x4、2x2、1x1大小的特征图，我们在这三个特征图上每个点上都设置三个不同大小的anchor。当然，这只是一个例子，实际的SSD模型，在300x300的输入下，anchor数量也特别多，其在38x38、19x19、10x10、5x5、3x3、1x1的六个特征图上，每个点分别设置4、6、6、6、6、4个不同大小和长宽比的anchor，所以一共有**38x38x4+ 19x19x6+ 10x10x6+ 5x5x6+ 3x3x4+ 1x1x4= 8732个anchor。**

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-c9019da4502b907c48bf47542201ebcc_r.jpg" alt="img" style="zoom:67%;" />

借助神经网络强大的拟合能力，我们不再需要计算Haar、Hog等特征，直接让神经网络输出，**每个anchor是否包含（或者说与物体有较大重叠，也就是IoU较大）物体，以及被检测物体相对本anchor的中心点偏移以及长宽比例。**以下图为例：

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-f162eefb4af511d06f22bb9347d44f08_r.jpg" alt="img" style="zoom:67%;" />

一般的目标检测网络可能有成千上万个anchor，例如标准SSD在300x300输入下有8732个anchor，在500x500下anchor数量过万。我们拿上图中的三个anchor举例，神经网络的输出，**也就是每个anchor认为自己是否含有物体的概率，物体中心点与anchor自身的中心点位置的偏移量，以及相对于anchor宽高的比例**。**因为anchor的位置都是固定的，所以就可以很容易的换算出来实际物体的位置**。以图中的小猫为例，红色的anchor就以99%的概率认为它是一只猫，并同时给出了猫的实际位置相对于该anchor的偏移量，这样，**我们将输出解码后就得到了实际猫的位置**，如果它能通过NMS（非最大抑制）筛选，它就能顺利的输出来。但是，绿色的anchor就认为它是猫的概率就很小，紫色的anchor虽然与猫有重叠，但是概率只有26%。

其实SSD的**推理**很简单，就是根据anchor进行位置解码，然后进行NMS过程，就完成了推理。在**训练**的时候，也就是给每张图片的物体的Bounding Box，**相对于anchor进行编码，如果物体的Bounding Box与某个anchor的IoU较大，例如大于0.5就认为是正样本**，否则是负样本（当然，也有算法将大于0.7的设为正样本，小于0.3的算负样本，中间的不计算损失）。



## Anchor的宿命

**每一个anchor都将成为最终的预测框作为此生的荣誉，但被时代(网络)选中的却寥寥无几，大多数却是默默无闻，始于平凡，终于平凡。**

以SSD作者给出的示例图为例，图中有一只猫和一只狗，这只猫在8x8的特征图上所设置anchor中，有两个（蓝色部分）与猫的IoU较大，**可以认为是正样本（天选之子）**，而对于狗，在4x4的特征图上的设置的anchor，有一个（红色部分）与狗的IoU较大，可以认为是正样本。其他的，**都算作负样本(天气弃子)**。在实际中，因为anchor非常密集，所以SSD算法中，会有多个anchor与物体的IoU大于阈值，所以可能多个anchor都是对应同一个物体的正样本（例如这只猫，就可能有不止2个匹配的正样本）。所以说有的anchor一出生就有一个美好的未来，能够参与到最终预测结果的大赛中，虽然最终胜出的寥寥无几，但至少还有参与机会，而大部分anchor注定被网络所抛弃，此生都默默无闻。

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-6b7301961c07a52977d5f728007843ea_r.jpg" alt="img" style="zoom:67%;" />

一个anchor诞生的目的就是要像GT学习，越像越好（就是位置、宽高几乎一样）

同时代的检测器有R-CNN，人家预测的是偏移量。什么是偏移量？

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-4883b178ed0e2bb95f1d504dc6bed6a7_r.jpg" alt="preview" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20220827205819763.png" alt="image-20220827205819763" style="zoom: 67%;" />

之前YOLO v1直接预测x,y,w,h，范围比较大，现在我们想预测一个稍微小一点的值，来增加准确度。不得不先介绍2个新概念：**基于grid的偏移量和基于anchor的偏移量**。什么意思呢？

- **基于anchor的偏移量**的意思是，anchor的位置是固定的，**偏移量=目标位置-anchor的位置**。
- **基于grid的偏移量**的意思是，grid的位置是固定的，**偏移量=目标位置-grid的位置**。



## Anchor的竞争



## 参考

[目标检测中Anchor的本质分析](https://zhuanlan.zhihu.com/p/84398108)
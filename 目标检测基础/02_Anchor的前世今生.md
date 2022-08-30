# Anchor的前世今生

## **Anchor缘起**

**一开始YOLO v1的初始训练过程很不稳定**，在YOLO v2中，作者观察了很多图片的所有Ground Truth，发现：比如车，GT都是矮胖的长方形，再比如行人，GT都是瘦高的长方形，且宽高比具有相似性。那**能不能根据这一点，从数据集中预先准备几个几率比较大的bounding box，再以它们为基准进行预测呢？**这就是Anchor的初衷。



## Anchor的诞生

怎么设计



## Anchor最终的命运

一个anchor诞生的目的就是要像GT学习，越像越好（就是位置、宽高几乎一样）

同时代的检测器有R-CNN，人家预测的是偏移量。什么是偏移量？

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/v2-4883b178ed0e2bb95f1d504dc6bed6a7_r.jpg" alt="preview" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/kongyan66/Img-for-md/master/img/image-20220827205819763.png" alt="image-20220827205819763" style="zoom: 67%;" />

之前YOLO v1直接预测x,y,w,h，范围比较大，现在我们想预测一个稍微小一点的值，来增加准确度。不得不先介绍2个新概念：**基于grid的偏移量和基于anchor的偏移量**。什么意思呢？

- **基于anchor的偏移量**的意思是，anchor的位置是固定的，**偏移量=目标位置-anchor的位置**。
- **基于grid的偏移量**的意思是，grid的位置是固定的，**偏移量=目标位置-grid的位置**。



## Anchor的竞争
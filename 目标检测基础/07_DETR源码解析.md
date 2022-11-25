## 问题

DETR可谓是是Transformer在目标检测领域的开山之作了，非常经典，作为入门Transformer的必读之选，主要对代码结构及实现细节进行解读。

## 前言

拿到一个开源项目代码，要有马上配置环境能够正常运行Debug，并且通过解析train.py马上找到主要模型相关的内容，然后着重关注模型方面的解析，像一些日志、计算mAP、画图等等代码，完全可以不看，可以省很多时间，所以以后我讲解源码都会把无关的代码完全剥离，不再讲解，全部精力关注模型、改进、损失等内容。

Github注释版源码：[HuKai97/detr-annotations](https://github.com/HuKai97/detr-annotations)

## 整体架构

说明下整个网络的基本架构(组件)

## DETR主干

DETR主干分为两部分：CNN+Transformer

### BackBone



### Tranformer



## 损失函数 + 后处理 



## Dataset处理

采用coco数据集，处理过程一致。

## 源码学习重点

- backbone：Positional Encoding（PositionEmbeddingSine）；
- Transformer：TransformerEncoderLayer + TransformerDecoderLayer；
- 损失函数：匈牙利算法，二分图匹配（self.matcher）
- 后处理：PostProcess

## 参考

[【DETR源码解析】一、整体模型解析](https://blog.csdn.net/qq_38253797/article/details/127618806)  目前见过最好的代码解析了


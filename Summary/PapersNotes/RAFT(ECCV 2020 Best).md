### RAFT（ECCV 2020 best)

**Paper: RAFT: Recurrent All-Pairs Field Transforms for Optical Flow**

<img src = "C:\Users\陈勇虎\Desktop\Daily-Summary\Summary\images\RAFT1.png" align="center" style="width:90%">

**简述**

RAFT 提取每个像素的特征，为所有像素对构建多尺度 4D 相关体，并通过对相关体执行查找,并通过循环单元迭代更新流场。 

**Challenges：fast-moving objects, occlusions, motion blur, and textureless surfaces.**

数据项：相似图像区域对齐；正则项：运动合理性先验。

RAFT: SOTA, strong generalization, high efficiency.

RAFT三个主要部分:

* 一个特征编码器，为每个像素提取一个特征向量

* 一个相关层，为所有像素对产生 4D 相关体(4D correlation volume)，随后池化以产生较低分辨率的体积

* 一个循环的基于 GRU 的更新算子(update operator)，它从相关体中检索值并迭代更新初始化为零的流场。 

<img src = "C:\Users\陈勇虎\Desktop\Daily-Summary\Summary\images\RAFT1.png" align="center" style="width:100%">

结构如上图所示，RAFT的3 个主要组件的详细描述：（1）从两个输入图像中提取每像素特征的特征编码器，以及仅从 $I_1$ 中提取特征的上下文编码器。 (2) 相关层，通过取所有特征向量对的内积构造一个4D的W × H × W × H 相关体。 4D 体积的最后 2 个维度在多个尺度上汇集以构建一组多尺度体积。 (3) 一个更新算子，它通过使用当前估计从相关体积集合中查找值来循环更新光流。 

RAFT 架构受到传统的基于优化的方法的启发。 特征编码器提取每个像素的特征。 相关层计算像素之间的视觉相似度。 更新运算符模仿迭代优化算法的步骤。 但与传统方法不同，特征和运动先验是学习得到的——分别由特征编码器和更新算子学习。

**相关工作(重要)，需要详读其中涉及的几篇论文。**

* **Optical Flow vs Energy minimization**
* **Direct Flow Prediction**
* **Iterative Refinement**
* **Learning to Optimize**

**Approach**

给定一对连续的RGB图像$I_1,I_2$，估计流($f^1,f^2$)可以映射到对应的坐标上:$(u^{\prime},v^{\prime})=(u+f^1(u),v+f^2(v))$。

分为三个阶段:(1) 特征提取 (2) 计算视觉相似度 (3)迭代更新

**特征提取**

<img src = "C:\Users\陈勇虎\Desktop\Daily-Summary\Summary\images\RAFT2.png" align="center" style="width:50%">



特征提取通过卷积网络实现，特征编码器对 $I_1$ 和 $I_2$ 使用并将其映射到较低的分辨率上。编码器 $g_\theta$ 将会生成 1/8 分辨率的特征图，即 $g_\theta:\mathbb{R}^{H\times W \times 3}\longmapsto \mathbb{R}^{H/8\times W/8\times D}$，这里 $D=256$ 。特征编码器由6个残差块组成，每降低 1/2 分辨率使用两个，最后将特征图的分辨率降至原图的 1/8。

**计算视觉相似度**

输入的图片特征$g_\theta(I_1)\in \mathbb{R}^{H\times W \times D}$ ，$g_\theta(I_2)\in \mathbb{R}^{H\times W \times D}$ ，correlation volume由特征矢量每一对的点积计算而来。即有:
$$
\boldsymbol{C}(g_\theta(I_1),g_\theta(I_2)) \in \mathbb{R}^{H\times W \times H \times W}，C_{i,j,k,l} = \sum_hg_\theta(I_1)_{ijh}\cdot g_\theta(I_2)_{klh}
$$

**Correlations Pyramid**














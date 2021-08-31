[toc]

# 评价指标

基础的评价指标有 **(EndPoint Error)EPE**, 是估计值和真值之间的欧氏距离。

除此以外还有几个常用的指标：

1. **Average Angular Error(AAE)**
2. **Average Endpoint  Error(AEE)**
3. **Root-Mean-Square Error(RMSE)**
4. **The percentage of outliers averaged over all pixels(Fl-all)**

$(u_{*},v_{*})$ = ground truth flow $(u,v)$ = estimated flow

于是有:

|              Metric              |                           Formula                            |
| :------------------------------: | :----------------------------------------------------------: |
|  **Average Angular Error(AAE)**  | $1/HW\sum\arccos\left[(u_{*}u + v_{*}v + 1) / \sqrt{(u_{*}^{2} + v_{*}^{2} + 1)(u^2 + v^2 + 1)})\right]$ |
| **Average Endpoint  Error(AEE)** |           $1/HW\sum\sqrt{(u_{*}-u)^2+(v_{*}-v)^2}$           |
| **Root-Mean-Square Error(RMSE)** |      $\sqrt{1/HW\sum_{x,y}(I_{warped}(x,y)-I(x,y))^2}$       |

假设像素集合 $B_1$ 满足$EPE > 5$, 满足下式的像素集合为 $B_2$。
$$
\frac{EPE}{\sqrt{(u_{*} + v_{*})^2+10^{-5}}} \gt 5\%
$$
定义劣点集合 $B$ 为 $B_1 \cup B_2$，记 $N$ 为 坏点的个数。于是 **Fl-all** 可以定义为
$$
Fl-all = \frac{N}{HW} \times 100 \%
$$
其中 **AE** 的理解可以参考论文[^1], 光流表示为 $(u,v) = (u,v,1)$，**后者的单位为(pixels，pixels，frame)**

<img src = "\images\AAE.png" align="center" style="width:50%">

# 发展

《Optical Flow and Scene Flow Estimation: A Survey》 [^2]中给出了 **data-driven**和 **hybrid-driven**的光流估计网络，发展如下所示，具体可参考论文内容。

<img src = "\images\Survey-Zhai2021.png" align="center" style="width:90%">

## 分类

即为 **knowledge-driven**, **data-driven** 和 **hybrid-driven**三种，不过根据性能，后两种将成为未来的主流。

### U-Net

#### SPynet  









### Spatial pyramid network



[^1]:Barron, J.L., Fleet, D.J. & Beauchemin, S.S. Performance of optical flow techniques. *Int J Comput Vision* **12,** 43–77 (1994). https://doi.org/10.1007/BF01420984
[^2]:Zhai, Mingliang, Xuezhi Xiang, Ning Lv, and Xiangdong Kong. 2021. “Optical Flow and Scene Flow Estimation: A Survey.” *Pattern Recognition* 114 (June): 107861. https://doi.org/10.1016/j.patcog.2021.107861.


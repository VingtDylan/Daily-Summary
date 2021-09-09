[toc]

# PWCNet Fusion (WACV 2019)

**Paper : A Fusion Approach for Multi-Frame Optical Flow Estimation**

**Architecture of the proposed fusion approach for three-frame optical flow estimation**

<img src = "./images/PWCNetFusion1.png" align="center" style="width:90%">

Key ideas:

- If we are given $f_{t-1\to t}$ and $f_{t\to t-1}$, and assume constant velocity of movement, then an estimate of $f_{t\to t+1}$ can be formed by backward warping $f_{t-1\to t}$ with $f_{t\to t-1}$.

- With three frames available, we can plug-in any two-frame optical flow estimation solution (PWCNet in this case) to obtain $f_{t-1 \to t}$, $f_{t\to t+1}$ and $f_{t \to t-1}$.

- A fusion network (similar to the one used in the last stage of FlowNet 2.0) can be used to fuse together and.

  - Note that would be identical to if
    * (a) velocity is constant 
    * (b) three optical flow estimations are correct
    * (c) there are no occlusions
  
  	Brightness constancy errors of the two flow maps together with the source frame $I_t$ are fed into the fusion network to provide additional info.

**Why multi-frame may perform better than 2-frame solutions:**

- temporal smoothness leads to additional regularization.

- longer time sequences may help in ambiguous situations such as occluded regions.

本文提出了基于深度学习的方法框架，分别是 **FlowNetS++** , **FlowNetS + GRU**，**PWC-Net + GRU**模型。从模型上看，框架中将会把从前几个图片对中得到的信息带入到后面的帧中进行处理。循环神经网络在处理时序信号上的优势也正是应用它的关键所在，同时，GRU模型较小，使用GRU从视频流中捕获特征也更有优势。

<img src = "./images/PWCNetFusion2.png" align="center" style="width:90%">

在 **PWC-Net + GRU**结构中，是通过在GRU-RCN的不同层级上输入编码后的特征，在不同的层级上解码特征和学习特征表示。

论文采用了PWC-Net模型中的训练损失函数:
$$
L(\Theta)=\sum_{l = l_0}^{L}\alpha_l\sum_{x}(|w_\Theta^l(x)-w_{GT}^l(x)|+\epsilon)^q + \gamma||\Theta||_2^2
$$
在后续的消融分析上，作者通过实验也发现，使用三帧图片的确可以带来更好的数据结果，而且在和两帧方法相比之后，该文提出的融合网络方法也达到了更好的效果。

<img src = "./images/PWCNetFusion3.png" align="center" style="width:90%">


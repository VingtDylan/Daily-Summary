详细讲解参考[链接](https://krasjet.github.io/quaternion/bonus_gimbal_lock.pdf)

先知概念:

* [**Euler angles**](https://en.jinzhao.wiki/wiki/Euler_angles)
* **Gimbal Lock** **万向锁**
* *yaw, pitch, roll** 偏航-俯仰-滚转
  * 绕物体的 Z 轴旋转，得到偏航角 yaw
  * 绕旋转之后的 Y 轴旋转，得到俯仰角 pitch
  * 绕旋转之后的 X 轴旋转，得到滚转角 roll



**三维空间的旋转**

欧拉角的表示方法会导致**Gimbal Lock**问题，而且依赖于坐标轴的选定，因此考虑轴角式的旋转。

考虑将一个向量$\boldsymbol{v}$，沿着旋转轴$\boldsymbol{u}=(x,y,z)^{T}$旋转$\theta$度，得到$\boldsymbol{v}^{\prime}$:

<img src = "\images\Axis-angle.png" align="center" style="width:35%">

先进行旋转的分解，把$\boldsymbol{v}$分解成**平行**于旋转轴$\boldsymbol{u}$以及**正交**于$\boldsymbol{u}$的两个分量：$\boldsymbol{v}_{\parallel},\boldsymbol{v}_{\perp}$，即：
$$
\boldsymbol{v} = \boldsymbol{v}_{\parallel} + \boldsymbol{v}_{\perp}
$$
可以分别旋转这两个分向量，再将他们旋转的结果相加获得旋转后的向量：
$$
\boldsymbol{v}^{\prime} = \boldsymbol{v}_{\parallel}^{\prime} + \boldsymbol{v}_{\perp}^{\prime}
$$
<img src = "\images\factorization.png" align="center" style="width:35%">

从正交投影公式，可以得出:
$$
\boldsymbol{v}_{\parallel} = proj_u{\boldsymbol{v}} = \frac{\boldsymbol{u}\cdot\boldsymbol{v}}{||\boldsymbol{u}||^2}\boldsymbol{u} = (\boldsymbol{u}\cdot\boldsymbol{v})\boldsymbol{u}
$$
由于$\boldsymbol{v} = \boldsymbol{v}_{\parallel} + \boldsymbol{v}_{\perp}$，于是有：$\boldsymbol{v}_{\perp} = \boldsymbol{v} - \boldsymbol{v}_{\parallel} = \boldsymbol{v} - (\boldsymbol{u}\cdot\boldsymbol{v})\boldsymbol{u}$

对于$\boldsymbol{v}_{\parallel}$的旋转，仍然与旋转轴$\boldsymbol{u}$重合，因此$\boldsymbol{v}_{\parallel}^{\prime}=\boldsymbol{v}_{\parallel}$

对于$\boldsymbol{v}_{\perp}$，利用三角的知识可以得到:

<img src = "\images\rotate-perp.png" align="center" style="width:55%">
$$
\begin{align}
\boldsymbol{v}_{\perp}^{\prime}&=\boldsymbol{v}_{v}^{\prime}+\boldsymbol{v}_{w}^{\prime}\notag\\
&= \cos(\theta)\boldsymbol{v}_{\perp}+\sin(\theta)\boldsymbol{w}\notag\\
&= \cos(\theta)\boldsymbol{v}_{\perp}+\sin(\theta)(\boldsymbol{u}\times\boldsymbol{v}_{\perp})
\end{align}
$$
从而有:
$$
\begin{align}
\boldsymbol{v}^{\prime} &= \boldsymbol{v}_{\parallel}^{\prime} + \boldsymbol{v}_{\perp}^{\prime}\notag \\
&=\boldsymbol{v}_{\parallel} + \cos(\theta)\boldsymbol{v}_{\perp}+\sin(\theta)(\boldsymbol{u}\times\boldsymbol{v}_{\perp})\notag\\
&=(\boldsymbol{u}\cdot\boldsymbol{v})\boldsymbol{u}+\cos(\theta)(\boldsymbol{v} - (\boldsymbol{u}\cdot\boldsymbol{v})\boldsymbol{u})+\sin(\theta)(\boldsymbol{u}\times\boldsymbol{v})\notag\\
&=\cos(\theta)\boldsymbol{v} +(1-\cos(\theta)) (\boldsymbol{u}\cdot\boldsymbol{v})\boldsymbol{u}+\sin(\theta)(\boldsymbol{u}\times\boldsymbol{v})
\end{align}
$$

**Quaternions** **(四元数)**


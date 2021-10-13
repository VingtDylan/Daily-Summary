# 激活函数

整理了一下主要的激活函数。

* Logistic，sigmoid， soft step
  $$
  \sigma(x)=\frac{1}{1+e^{-x}}
  $$
  
* tanh

$$
\tanh(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}
$$

* RELU
  $$
  \begin{aligned}
  	 &{\begin{cases}
         0&{\text{if }}x\leq 0\\
         x&{\text{if }}x>0
         \end{cases}}\\
  {}={}&\max\{0,x\}=x{\textbf {1}}_{x>0}
  \end{aligned}
  $$

* GELU
  $$
  \begin{aligned}
       &{\frac {1}{2}}x\left(1+{\text{erf}}\left({\frac {x}{\sqrt {2}}}\right)\right)\\
  {}={}&x\Phi (x)
  \end{aligned}
  $$

* softplus
  $$
  \ln(1+e^x)
  $$

* ELU
  $$
  \begin{cases}
  	\alpha \left(e^{x}-1\right)&{\text{if }}x\leq 0\\
  	x&{\text{if }}x>0
  \end{cases}
  $$

* SELU
  $$
  \lambda\begin{cases}
  	\alpha \left(e^{x}-1\right)&{\text{if }}x\leq 0\\
  	x&{\text{if }}x>0
  \end{cases}
  $$

* Leaky RELU
  $$
  \begin{cases}
  	0.01x&{\text{if }}x<0\\
  	    x&{\text{if }}x\geq 0
  \end{cases}
  $$

* PRELU
  $$
  \begin{cases}
  	\alpha x&{\text{if }}x<0\\
  	    x&{\text{if }}x\geq 0
  \end{cases}
  $$

* SiLU
  $$
  \frac{x}{1+e^{-x}}
  $$

* Mish
  $$
  x\tanh(\ln(1+e^x))
  $$


[toc]

# 相关概念

参考oiwiki [图论相关概念](https://oi-wiki.org/graph/concept/)

**自环 (Loop)**：对 **E** 中的边 **e = (u, v)**，若 **u = v** ，则 **e** 被称作一个自环。

**重边 (Multiple edge)**：若 **E** 中存在两个完全相同的元素（边）$e_1$ , $e_2$，则它们被称作（一组）重边。

**简单图 (Simple graph)**：若一个图中没有自环和重边，它被称为简单图。具有至少两个顶点的简单无向图中一定存在度相同的结点。（[鸽巢原理](https://oi-wiki.org/math/combinatorics/drawer-principle/)）

如果一张图中有自环或重边，则称它为 **多重图 (Multigraph)**。

**子图(subgraph)**

**导出子图/诱导子图(Induced subgraph)** $(u,v)\in E \rightarrow (u,v)\in E^{\prime}$

**生成子图、支撑子图(Spanning subgraph)**  $V^{\prime} = V$

若一张图的边数远小于其点数的平方，那么它是一张 **稀疏图 (Sparse graph)**。

若一张图的边数接近其点数的平方，那么它是一张 **稠密图 (Dense graph)**。

**补图** 无向简单图，$V(\bar{G}) = V(G) \&\&((u,v) \in E(\bar{G}) \iff (u,v) \notin E(G))$

**反图** 有向图，$G^{\prime} = (V, E^{\prime}) \quad E^{\prime}=\{(v,u)|(u,v)\in E \}$

**完全图(Complete graph)**，n阶完全图($K_n$)，**完全有向图(Complete digraph)**

边集为空：**零图(Null graph)** ，n阶零图($N_n$)，$N_n$ 和 $K_n$互为补图

若有向简单图 $G$ 满足任意不同两点间都有恰好一条边（单向），则称 $G$ 为 **竞赛图 (Tournament graph)**。

# 存储

参考oiwiki [图的存储](https://oi-wiki.org/graph/save/)

直接存边

邻接矩阵

邻接表

链式前向星 == 链表实现邻接表

```c++
// head[u] 和 cnt 的初始值都为 -1
void add(int u, int v) {
  nxt[++cnt] = head[u];  // 当前边的后继
  head[u] = cnt;         // 起点 u 的第一条边
  to[cnt] = v;           // 当前边的终点
}

// 遍历 u 的出边
for (int i = head[u]; ~i; i = nxt[i]) {  // ~i 表示 i != -1
  int v = to[i];
}
```

#  DFS


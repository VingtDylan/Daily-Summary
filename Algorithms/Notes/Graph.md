[toc]

## 相关概念

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

## 存储

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

##  DFS

参考oiwiki[DFS(图论)](https://oi-wiki.org/graph/dfs/)

## BFS

参考oikiwi[DFS(图论)](https://oi-wiki.org/graph/bfs/)

应用

- 在一个无权图上求从起点到其他所有点的最短路径。
- 在 $O(n + m)$ 时间内求出所有连通块。（我们只需要从每个没有被访问过的节点开始做 BFS，显然每次 BFS 会走完一个连通块）
- 如果把一个游戏的动作看做是状态图上的一条边（一个转移），那么 BFS 可以用来找到在游戏中从一个状态到达另一个状态所需要的最小步骤。
- **在一个边权为 0/1 的图上求最短路。（需要修改入队的过程，如果某条边权值为 0，且可以减小边的终点到图的起点的距离，那么把边的起点加到队列首而不是队列尾）**
- **在一个有向无权图中找最小环。（从每个点开始 BFS，在我们即将抵达一个之前访问过的点开始的时候，就知道遇到了一个环。图的最小环是每次 BFS 得到的最小环的平均值。）**
- **找到一定在 $(a,b) $ 最短路上的边。（分别从 a 和 b 进行 BFS，得到两个 d 数组。之后对每一条边 $(u,v)$，如果 $d_a[u] + 1 + d_b[v] = d_a[b]$ ，则说明该边在最短路上）**
- **找到一定在 $(a,b)$ 最短路上的点。（分别从 a 和 b 进行 BFS，得到两个 d 数组。之后对每一个点 v，如果 $d_a[u] + d_b[v] = d_a[b]$ ，则说明该点在最短路上）**
- :sweat_smile:**找到一条长度为偶数的最短路。（我们需要一个构造一个新图，把每个点拆成两个新点，原图的边 $(u,v)$ 变成 $((u,0),(v,1))$ 和 $((u,1),(v,0))$ 。对新图做 BFS，$(s,0)$ 和 $(t,0)$ 之间的最短路即为所求）**

**双端队列(0-1 BFS)**

参考oiwiki [STL Deque库](https://oi-wiki.org/lang/csl/sequence-container/#deque)

**优先队列 BFS**

优先队列，相当于一个二叉堆，STL 中提供了 [`std::priority_queue`](https://oi-wiki.org/lang/csl/container-adapter/#_13)，可以方便我们使用优先队列。

## 拓扑排序

参考oiwki[拓扑排序](https://oi-wiki.org/graph/topo/)

应用：

1. 拓扑排序可以用来判断图中是否有环
2. 还可以用来判断图是否是一条链
3. 求字典序最大/最小的拓扑排序 （优先队列维护Kahn算法中的队列）

## 最小生成树

参考oiwiki[最小生成树](https://oi-wiki.org/graph/mst/)

[次小生成树](https://oi-wiki.org/graph/mst/#_9)

## 最短路（重点）

参考oiwiki[最短路](https://oi-wiki.org/graph/shortest-path/)

不同方法的比较

| 最短路算法       | Floyd                | Bellman-Ford | Dijkstra     | Johnson              |
| :--------------- | :------------------- | :----------- | :----------- | :------------------- |
| 最短路类型       | 每对结点之间的最短路 | 单源最短路   | 单源最短路   | 每对结点之间的最短路 |
| 作用于           | 没有负环的图         | 任意图       | 非负权图     | 没有负环的图         |
| 能否检测负环？   | 能                   | 能           | 不能         | 不能                 |
| 推荐作用图的大小 | 小                   | 中/小        | 大/中        | 大/中                |
| 时间复杂度       | $O(N^3)$             | $O(NM)$      | $O(M\log M)$ | $O(NM\log M)$        |

## 二分图

参考oiwiki[二分图](https://oi-wiki.org/graph/bi-graph/)
















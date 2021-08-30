八皇后到N皇后遇到的一些题



**八皇后问题**

[LeetCode 面试题08.12](https://leetcode-cn.com/problems/eight-queens-lcci/) 求具体方案

```c++
class Solution {
public:
    vector<bool> col, dg, udg;
    int size;
    vector<vector<string>> solveNQueens(int n) {
        col.resize(n, false), size = n;
        dg.resize(2 * n, false), udg.resize(2 * n, false);
        vector<vector<string>> res;
        vector<int> ans(n, 0);
        dfs(0, ans, res);
        return res;
    }

    void dfs(int x, vector<int>& ans, vector<vector<string>>& res){
        if(x == size){
            vector<string> temp(size, string(size, '.'));
            for(int i = 0; i < size; i++){
                temp[i][ans[i]] = 'Q';
            }
            res.push_back(temp);
            return;
        }   
        for(int y = 0; y < size; y++){
            if(!col[y] && !dg[y + x] && !udg[y - x + size]){
                ans[x] = y;
                col[y] = dg[y + x] = udg[y - x + size] = true;
                dfs(x + 1, ans, res);
                col[y] = dg[y + x] = udg[y - x + size] = false;
            }
        }
    }
};
```

**N皇后问题**

[LeetCode 51.N皇后](https://leetcode-cn.com/problems/n-queens/)和前面同一题题目，也是求普通N皇后的具体方案，直接CV

```c++
    vector<bool> col, dg, udg;
    int size;
    vector<vector<string>> solveNQueens(int n) {
        col.resize(n, false), size = n;
        dg.resize(2 * n, false), udg.resize(2 * n, false);
        vector<vector<string>> res;
        vector<int> ans(n, 0);
        dfs(0, ans, res);
        return res;
    }

    void dfs(int x, vector<int>& ans, vector<vector<string>>& res){
        if(x == size){
            vector<string> temp(size, string(size, '.'));
            for(int i = 0; i < size; i++){
                temp[i][ans[i]] = 'Q';
            }
            res.push_back(temp);
            return;
        }   
        for(int y = 0; y < size; y++){
            if(!col[y] && !dg[y + x] && !udg[y - x + size]){
                ans[x] = y;
                col[y] = dg[y + x] = udg[y - x + size] = true;
                dfs(x + 1, ans, res);
                col[y] = dg[y + x] = udg[y - x + size] = false;
            }
        }
    }
```

**N皇后II**

[LeetCode II](https://leetcode-cn.com/problems/n-queens-ii/)区别就是求方案数了，不需要输出方案而已，稍微修改一下遍历结束的逻辑即可

```c++
class Solution {
public:
    vector<bool> col, dg, udg;
    int size;
    int totalNQueens(int n) {
        col.resize(n, false), size = n;
        dg.resize(2 * n, false), udg.resize(2 * n, false);
        vector<int> ans(n, 0);
        int res = 0;
        dfs(0, res, ans);
        return res;
    }

    void dfs(int x, int& res, vector<int>& ans){
        if(x == size){
            res++;
            return;
        }   
        for(int y = 0; y < size; y++){
            if(!col[y] && !dg[y + x] && !udg[y - x + size]){
                ans[x] = y;
                col[y] = dg[y + x] = udg[y - x + size] = true;
                dfs(x + 1, res, ans);
                col[y] = dg[y + x] = udg[y - x + size] = false;
            }
        }
    }
};    
```

**棋盘挑战**

[Acwing棋盘挑战](https://www.acwing.com/problem/content/description/1434/) 就是既求具体方案(天生的字典序可以忽略字典序的要求了。。。)和方案数而已，mix一下。

```c++
#include <iostream>

using namespace std;

const int N = 15;
int col[N], dg[N * 2], udg[N * 2];
int path[N], ans, n;

void dfs(int x){
    if(x > n){
        ans ++;
        if(ans <= 3){
            for(int i = 1; i <= n; i++) cout << path[i] << " ";
            cout << endl;   
        }
        return;
    }
    for(int y = 1; y <= n; y++){
        if(!col[y] && !dg[x + y] && !udg[y - x + n]){
            path[x] = y;
            col[y] = dg[x + y] = udg[y - x + n] = true;
            dfs(x + 1);
            col[y] = dg[x + y] = udg[y - x + n] = false;
        }
    }
}

int main(){
    cin >> n;
    dfs(1);
    cout << ans << endl;
    return 0;
}
```

**八皇后 new**

[Acwing 3472 八皇后](https://www.acwing.com/problem/content/3475/)输出第n个方案。

```c++
#include <iostream>

using namespace std;

const int N = 15, M = 100, n = 8;
int col[N], dg[N * 2], udg[N * 2];
int path[N], ans;
int res[M][N];

void dfs(int x){
    if(x > n){
        ans ++;
        for(int i = 1; i <= n; i++) res[ans][i] = path[i];
        return;
    }
    for(int y = 1; y <= n; y++){
        if(!col[y] && !dg[x + y] && !udg[y - x + n]){
            path[x] = y;
            col[y] = dg[x + y] = udg[y - x + n] = true;
            dfs(x + 1);
            col[y] = dg[x + y] = udg[y - x + n] = false;
        }
    }
}

int main(){
    dfs(1);
    int t; cin >> t;
    while (t -- ){
        int k;cin >> k;
        for(int i = 1; i <= n; i++)
            cout << res[k][i];
        cout << endl;
    }
    return 0;
}
```

**2n皇后问题**

蓝桥杯我一直登录不上去，思路就是先放一种，再放第二种皇后而已。



比特位等优化不赘述了。




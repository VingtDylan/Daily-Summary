# 树状数组( Binary Index Tree)

## 概念

概念等百度等都有。

**前缀和**方面有重要作用。

## 相关操作

相关操作

1. 修改

   ```c++
   void add(int x, int y){
       for(; x <= N; x += x & -x) c[x] = y;
   }
   ```

2. 查询

   ```c++
   int ask(int x){
       int ans = 0;
       for(; x; x -= x) ans += c[x];
       return ans;
   }
   ```

3. lowbit运算

   ```c++
   int lowbit(int x){
       return x & -x;
   }
   ```

4. 区间加 & 区间求和

   若维护序列 $a$ 的差分数组 $b$， 此时我们对 $a$ 的一个前缀 $r$ 求和，即 $\sum_{i = 1}^ra_i$， 由差分数组的定义得: $a_i = \sum_{j = 1}^ib_j$
   
   推导:
   $$
   \begin{align}
   &\sum_{i = 1} ^ {r} a_i \notag \\
   = &\sum_{i = 1} ^ {r} \sum_{j = 1} ^ {i} b_j \notag \\
   = &\sum_{i = 1} ^ {r} b_i \times (r - i  + 1) \notag \\
   = &\sum_{i = 1} ^ {r} b_i \times (r + 1) - \sum_{i = 1} ^ {r} b_i \times i \notag 
   \end{align}
   $$
   区间和可以用两个前缀和相减得到，因此只需要维护两个树状数组分别为维护 $\sum b_i$ 和 $\sum i\times b_i$，就能实现区间求和。

##  相关的系列题目

学习阶段做过的题目, 二维TODO

### [楼兰图腾](https://www.acwing.com/problem/content/243/)

有范围的求大于n的数的个数。

```c++
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long ll;

const int N = 200010;
int n;
int a[N], c[N];
int gt[N], lt[N];

int lowbit(int x){
    return x & -x;
}

void add(int x, int y){
    for(int i = x; i <= n; i += lowbit(i)) c[i] += y;
}

int sum(int x){
    int res = 0;
    for(int i = x; i; i -= lowbit(i)) res += c[i];
    return res;
}

int main(){
    cin >> n;
    for(int i = 1; i <= n; i++) cin >> a[i];
    for(int i = 1; i <= n; i++){
        int y = a[i];
        gt[i] = sum(n) - sum(y);
        lt[i] = sum(y - 1);
        add(y, 1);
    }
    memset(c, 0, sizeof(c));
    ll res1 = 0, res2 = 0;
    for(int i = n; i > 0; i--){
        int y = a[i];
        res1 += gt[i] * (ll)(sum(n) - sum(y));
        res2 += lt[i] * (ll)sum(y - 1);
        add(y, 1);
    }
    cout << res1 << " " << res2 << endl;
    return 0;
}
```

### [一个简单的整数问题](https://www.acwing.com/problem/content/248/)

```c++
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long long ll;

const int N = 100010;
int a[N], c[N];
int n, m;

int lowbit(int x){
    return x & -x;
}

void add(int x, int y){
    for(int i = x; i <= n; i += lowbit(i)) c[i] += y;
}

ll sum(int x){
    ll res = 0;
    for(int i = x; i; i -= lowbit(i)) res += c[i];
    return res;
}

int main(){
    cin >> n >> m;
    for(int i = 1; i <= n; i++) cin >> a[i];
    for(int i = 1; i <= n; i++) add(i, a[i] - a[i - 1]);
    while(m--){
        string a;
        cin >> a;
        if(a == "Q"){
            int l;
            cin >> l;
            cout << sum(l) << endl;
        }else{
            int l, r, d;
            cin >> l >> r >> d;
            add(l, d), add(r + 1, -d);
        }
    }
    return 0;
}
```

### [一个简单的整数问题2](https://www.acwing.com/activity/content/problem/content/1594/)

$a_i$的差分序列为$b_i$，

$\sum_{i = 1}^{x}\sum_{j = 1}^{i}b[j]=(x+1)\sum_{i = 1}^{x}b[i]-\sum_{i = 1}^{x} i * b[i]$，

维护两个树状数组$c_1,c_2$，其中$c_1$维护$b_i$, $c_2$维护$i*b_i$。

```c++
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long long ll;

const int N = 100010;
int a[N];
ll c1[N], c2[N];
int n, m;
char op;
int l, r, d;

int lowbit(int x){
    return x & -x;
}

void add(ll c[], int x, ll y){
    for(int i = x; i <= n; i += lowbit(i)) c[i] += y;
}

ll sum(ll c[], int x){
    ll res = 0;
    for(int i = x; i; i -= lowbit(i)) res += c[i];
    return res;
}

ll prefix(int x){
    return sum(c1, x) * (x + 1) - sum(c2, x);
}

int main(){
    cin >> n >> m;
    for(int i = 1; i <= n; i++) cin >> a[i];
    for(int i = 1; i <= n; i++){
        int b = a[i] - a[i - 1];
        add(c1, i, b);
        add(c2, i, (ll)b * i);
    }
    while(m--){
        cin >> op;
        if(op == 'Q'){
            cin >> l >> r;
            cout << prefix(r) - prefix(l - 1) << endl;
        }else{
            cin >> l >> r >> d;
            add(c1, l, d);
            add(c1, r + 1, -d);
            add(c2, l, (ll)l * d);
            add(c2, r + 1, (ll)(r + 1) * -d);
        }
    }
    return 0;
}
```

### [谜一样的牛](https://www.acwing.com/problem/content/245/)

```c++
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 100010;
int h[N], ans[N], c[N];
int n;

int lowbit(int x){
    return x & -x;
}

void add(int x, int y){
    for(int i = x; i <= n; i += lowbit(i)) c[i] += y;
}

int sum(int x){
    int res = 0;
    for(int i = x; i; i -= lowbit(i)) res += c[i];
    return res;
}

int main(){
    cin >> n;
    for(int i = 2; i <= n; i++) cin >> h[i];
    for(int i = 1; i <= n; i++) add(i, 1);
    for(int i = n; i; i--){
        int k = h[i] + 1;
        int l = 1, r = n;
        while(l < r){
            int mid = l + r >> 1;
            if(sum(mid) >= k) r = mid;
            else l = mid + 1;
        }
        ans[i] = r;
        add(r, -1);
    }
    for(int i = 1; i <= n; i++) cout << ans[i] << endl;
    return 0;
}
```

### [P3374](https://www.luogu.com.cn/problem/P3374)模板题

```c++
#include <iostream>

using namespace std;

typedef long long ll;

const int N = 500010;
int a[N], c[N];
int n, m;
int op, x, y, k;

int lowbit(int x){
    return x & -x;
}

void add(int x, ll y){
    for(int i = x; i <= n; i += lowbit(i)) c[i] += y;
}

ll sum(int x){
    ll res = 0;
    for(int i = x; i; i -= lowbit(i)) res += c[i];
    return res;
}

int main(){
    cin >> n >> m;
    for(int i = 1; i <= n; i++){
        cin >> a[i];
        add(i, a[i]);
    }
    for(int i = 1; i <= m; i++) {
        cin >> op;
        if(op == 1){
            cin >> x >> k;
            add(x, k);
        }else{
            cin >> x >> y;
            cout << sum(y) - sum(x - 1) << endl;
        }

    }
    return 0;
}

/*
 5 5
 1 5 4 2 3
 1 1 3
 2 2 5
 1 3 -1
 1 4 2
 2 1 4

 14
 16
 */
```

### [P3368](https://www.luogu.com.cn/problem/P3368)模板题

```c++
#include <iostream>

using namespace std;

const int N = 500010;
int a[N];
int c[N];
int n, m;
int op, l, r, k;

int lowbit(int x){
    return x & -x;
}

void add(int x, int y){
    for(int i = x; i <= n; i += lowbit(i)) c[i] += y;
}

int sum(int x){
    int res = 0;
    for(int i = x; i; i -= lowbit(i)) res += c[i];
    return res;
}

int main(){
    cin >> n >> m;
    for(int i = 1; i <= n; i++) cin >> a[i];
    for(int i = 1; i <= n; i++) add(i, a[i] - a[i - 1]);
    for(int i = 1; i <= m; i++){
        cin >> op;
        if(op == 1){
            cin >> l >> r >> k;
            add(l, k), add(r + 1, -k);
        }else{
            cin >> l;
            cout << sum(l) << endl;
        }
    }
    return 0;
}

/*
 5 5
 1 5 4 2 3
 1 2 4 2
 2 3
 1 1 5 -1
 1 3 5 7
 2 4

 6
 10
 */
```

### [315. 计算右侧小于当前元素的个数](https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/)

需要离散化才能过

也可以merge_sort

**树状数组**

```c++
class Solution {
private:
    vector<int> a;
    vector<int> c;
    int len;

    void init(int n){
        c.resize(n, 0);
        len = n - 1;
    }

    void dis(vector<int>& nums){
        a.assign(nums.begin(), nums.end());
        sort(a.begin(), a.end());
        a.erase(unique(a.begin(), a.end()), a.end());
    }

    int get_id(int x){
        return lower_bound(a.begin(), a.end(), x) - a.begin() + 1;
    }

    int lowbit(int x){
        return x & -x;
    }

    void add(int x, int y){
        for(int i = x; i <= len; i += lowbit(i)) c[i] += y;
    }

    int sum(int x){
        int res = 0;
        for(int i = x; i; i -= lowbit(i)) res += c[i];
        return res;
    }

public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> res;
        dis(nums);
        init(nums.size() + 10);
        for(int i = (int)nums.size() - 1; i >= 0; i--){
            int id = get_id(nums[i]);
            res.push_back(sum(id - 1));
            add(id, 1);
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```

**merge_sort思路**

```c++
class Solution {
public:
    vector<pair<int, int>> a;
    vector<pair<int, int>> b;
    vector<int> ans;
    vector<int> countSmaller(vector<int>& nums) {
        if (nums.empty()) return {};
        int n = nums.size();
        ans = vector<int>(n);
        b = vector<pair<int, int>> (n);
        for (int i = 0; i < n; i++) a.push_back({nums[i], i});
        merge_sort(a, 0, n - 1);
        return ans;
    }

    void merge_sort(vector<pair<int, int>>& a, int l, int r) {
        if (l == r) return;
        int mid = l + r >> 1;
        merge_sort(a, l, mid);
        merge_sort(a, mid + 1, r);
        int i = l, j = mid + 1, k = 0;
        while(i <= mid && j <= r){
            if (a[i].first <= a[j].first) {
                b[k++] = a[i];
                ans[a[i++].second] += j - mid - 1; 
            }
            else b[k++] = a[j++];
        }
        while (i <= mid) {
            ans[a[i].second] += r - mid; 
            b[k++] = a[i++];
        }
        while (j <= r) b[k++] = a[j++];
        for (int i = 0; i < k; i++) a[l + i] = b[i];
    }
};
```


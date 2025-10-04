#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

const int MaxN = 1 + 1e3;

int n, a[MaxN], b[MaxN], dp[MaxN];

int main(){
    freopen("bai2.inp","r",stdin);
    freopen("CTDL.out","w",stdout);
    cin >> n;
    for(int i = 1 ; i <= n ; ++i) cin >> a[i] >> b[i];
    dp[n] = a[n];
    for(int i = n - 1 ; i >= 1 ; --i) dp[i] = min(dp[i + 1] + a[i], dp[i + 2] + b[i]);
    cout << dp[1] << endl;

    return 0;
}

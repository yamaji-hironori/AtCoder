#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#ifdef _DEBUG
#define debug(x) cout<<#x<<": "<<x<<endl
#else
#define debug(x)
#endif

#define rep(i,n) for(size_t i=0;i<(n);++i)
int main(){
    int K = 10;
    int cnt = 0;
    rep(i, K){
        cnt++;
    }
    while (K) {
        K--;
        cnt++;
    }
    debug(cnt);
    return 0;
}

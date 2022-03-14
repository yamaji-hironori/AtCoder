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
    string S;
    cin >> S;
    ll cnt = 1;
    rep(i, S.size()) {
        if ((i % 2) == 0) {
            continue;
        }
        if (S.at(i) == '+') {
            cnt++;
        } else {
            cnt--;
        }
    }
    cout<<cnt<<endl;
    return 0;
}

#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vll = vector<ll>;
using vvll = vector<vll>;

#ifdef _DEBUG
#define debug(x) cout<<#x<<": "<<x<<endl
#define debug_vec(x) cout<<#x<<" ->"<<endl;for(size_t i=0;i<x.size();i++){cout<<x.at(i)<<"; ";}cout<<endl;
#define debug_vecvec(x) cout<<#x<<" ->"<<endl;for(size_t i=0;i<x.size();i++){for(size_t j=0;j<x[i].size();j++){cout<<x.at(i).at(j)<<"; ";}cout<<endl;}cout<<endl;
#else
#define debug(x)
#define debug_vec(x)
#define debug_vecvec(x)
#endif

#define rep(i,n) for(size_t i=0;i<(n);++i)
int main(){
    ll N;
    cin >> N;
    vll A(N);
    for (size_t i=0;i<N;i++) {
        cin >> A.at(i);
    }
    sort(A.begin(), A.end());
    ll ans = 0;
    rep(i, N) {
        if (find(A.begin(), A.end(), ans) == A.end()) {
            break;
        } else {
            ans++;
        }
    }
    cout << ans << endl;
    return 0;
}

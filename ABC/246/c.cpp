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
    ll N, K, X;
    cin >> N>>K>>X;
    vll A(N), mod_B(N);
    ll total_price = 0;
    rep(i, N) {
        cin>>A.at(i);
        total_price += A.at(i);
    }

    ll mod_cnt = 0;
    rep(i,N) {
        mod_cnt += A.at(i) / X;
    }

    ll now_K;
    if (mod_cnt >= K) {
        total_price -= K*X;
        cout << total_price << endl;
        return 0;
    } else {
        total_price -= mod_cnt*X;
        now_K = K - mod_cnt;
    }

    rep(i,N) {
        ll tmp = A.at(i) % X;
        mod_B.at(i) = tmp;
    }
    debug_vec(mod_B);
    sort(mod_B.begin(), mod_B.end()); // TODO
    ll i = 0;
    while (i<N && i<now_K) {
        ll j = N -1 -i;
        total_price -= mod_B.at(j);
        i++;
    }

    cout << total_price << endl;
    return 0;
}

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
    ll N, M;
    cin >> N >> M;
    vvll AB(N, vll(2)), CD(M, vll(2));
    rep(i, N) {
        cin >> AB.at(i).at(0);
    }
    rep(i, N) {
        cin >> AB.at(i).at(1);
    }
    rep(i, M) {
        cin >> CD.at(i).at(0);
    }
    rep(i, M) {
        cin >> CD.at(i).at(1);
    }
    sort(AB.begin(), AB.end(), [&](vll first, vll second){return first.at(0) > second.at(0);});
    sort(CD.begin(), CD.end(), [&](vll first, vll second){return first.at(0) > second.at(0);});
    debug_vecvec(AB);
    debug_vecvec(CD);

    multiset<ll> S;
    size_t j = 0;
    for (ll i=0;i<N;i++) {
        while (j<M and AB[i][0]<=CD[j][0]) {
            S.insert(CD[j][1]);
            j++;
        }
        if (S.lower_bound(AB[i][1]) == S.end()) {
            cout << "No" << endl;
            return 0;
        } else {
            S.erase(*S.lower_bound(AB[i][1]));
        }
    }
    cout << "Yes" << endl;
    return 0;
}


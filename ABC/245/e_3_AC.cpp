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
struct HW {
    ll H=0,W=0;
};
int main(){
    ll N, M;
    cin >> N >> M;
    vector<HW> Choco(N), Box(M);
    rep(i, N) {
        cin >> Choco.at(i).H;
    }
    rep(i, N) {
        cin >> Choco.at(i).W;
    }
    rep(i, M) {
        cin >> Box.at(i).H;
    }
    rep(i, M) {
        cin >> Box.at(i).W;
    }
    sort(Choco.begin(), Choco.end(), [&](HW first, HW second){return first.H > second.H;});
    sort(Box.begin(), Box.end(), [&](HW first, HW second){return first.H > second.H;});

    multiset<ll> S;
    ll j = 0;
    for (ll i=0;i<N;i++) {
        while (j<M and Choco[i].H<=Box[j].H) {
            S.insert(Box[j].W);
            j++;
        }
        auto iter = S.lower_bound(Choco[i].W);
        if (iter == S.end()) {
            cout << "No" << endl;
            return 0;
        } else {
            S.erase(iter);
        }
    }
    cout << "Yes" << endl;
    return 0;
}


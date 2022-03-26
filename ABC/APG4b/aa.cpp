#define _LIBCPP_DEBUG 0
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
    map<ll, ll> A_counter;
    rep(i,N){
        ll i_A;
        cin >> i_A;
        if (A_counter.count(i_A)) {
            A_counter.at(i_A)++;
        } else {
            A_counter[i_A] = 1;
        }
    }

    ll max_count = 0;
    ll max_A;
    for (auto pairs: A_counter) {
        auto i_A = pairs.first;
        auto i_count = pairs.second;
        if (max_count < i_count) {
            max_count = i_count;
            max_A = i_A;
        }
    }
    cout << max_A << " " << max_count << endl;
    return 0;
}

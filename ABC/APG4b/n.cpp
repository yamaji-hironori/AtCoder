#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#ifdef _DEBUG
#define debug(x) cout<<#x<<": "<<x<<endl
#define debug_vec(x) for(size_t i=0;i<x.size();i++){cout<<x.at(i)<<"; ";}cout<<endl;
#else
#define debug(x)
#define debug_vec(x)
#endif

#define rep(i,n) for(size_t i=0;i<(n);++i)
int main(){
    ll N;
    cin >> N;
    vector<ll> A(N);
    ll total = 0;
    rep(i, N) {
        cin>>A.at(i);
        total+=A.at(i);
    }
    debug_vec(A);
    ll average = total/N;
    rep(i,N) {
        cout<<abs(average-A.at(i))<<endl;
    }
    return 0;
}

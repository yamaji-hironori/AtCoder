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
    ll x1, y1;
    ll x2, y2;
    ll x3, y3;
    ll x4, y4;
    cin >> x1>>y1;
    cin >> x2>>y2;
    cin >> x3>>y3;
    if (x1 == x2) {
        x4 = x3;
    } else if (x2 == x3) {
        x4 = x1;
    } else {
        x4 = x2;
    }
    if (y1 == y2) {
        y4 = y3;
    } else if (y2 == y3) {
        y4 = y1;
    } else {
        y4 = y2;
    }
    
    cout << x4 << " " << y4 << endl;
    return 0;
}

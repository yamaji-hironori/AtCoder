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
    float A, B, Z;
    cin >> A >> B;
    Z = sqrt(A*A + B*B);
    debug(Z);

    float x, y;
    x = A / Z;
    y = B / Z;
    cout <<setprecision(7) << x << " " << y << endl;
    return 0;
}

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
ll N;
ll min_X = INFINITY;
ll binaly_search(ll a, ll left, ll right) {
    ll middle = (left + right) / 2;
    ll now_X = pow(a,3)+pow(a,2)*middle+a*pow(middle,2)+pow(middle,3);
    if (left == right || left == middle) {
        if (now_X >= N) {
            return now_X;
        } else {
            now_X = pow(a,3)+pow(a,2)*right+a*pow(right,2)+pow(right,3);
            return now_X;
        }
    }
    if (now_X == N) {
        return now_X;
    } else if (now_X > N) {
        right = middle;
    } else {
        left = middle;
    }
    return binaly_search(a, left, right);
}
int main(){
    ll a, b;
    cin >> N;
    a = pow(10, 6);

    while(a>-1) {
        ll right = a;
        ll left = 0;
        ll i_X = binaly_search(a, left, right);
        if (i_X >= N) {
            min_X = min(min_X, i_X);
        }
        a--;
    }
    cout << min_X << endl;
    return 0;
}

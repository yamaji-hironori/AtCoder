#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#ifdef _DEBUG
#define debug(x) cout<<#x<<": "<<x<<endl
#else
#define debug(x)
#endif

#define FOR(i,l,r) for(size_t i=(l);i<(r);++i)
#define REP(i,n) FOR(i,0,n)
int main(){
    ll N;
    cin >> N;
    vector<ll> A(N);
    vector<ll> B(N);
    for (ll i=0; i<N; i++){
        cin >> A[i];
    }
    for (ll i=0; i<N; i++){
        cin >> B[i];
    }

    // 同じ位置
    ll same_cnt = 0;
    for (ll i=0; i<N; i++){
        if (A[i] == B[i]) {
            same_cnt++;
        }
    }

    // 違う位置
    ll other_cnt = 0;
    for (ll i=0; i<N; i++){
        for (ll j=0; j<N; j++){
            if (i == j) {
                continue;
            }
            if (A[i] == B[j]) {
                other_cnt++;
            }
        }
    }
    cout << same_cnt << endl;
    cout << other_cnt << endl;
    return 0;
}

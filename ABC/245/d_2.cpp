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

void waru(ll &N, ll &M, vll &A, vll &B, vll &C, ll i) {
    debug(i);
    ll i_C = C.at(i);
    ll d_NM = (N+M) - i;
    for (ll j=0; j<(d_NM);j++) {
        if (N-d_NM+j < 0) {
            continue;
        }
        ll j_B = B.at(M-j);
        ll j_A = A.at(N-d_NM+j);
        i_C = i_C - (j_A * j_B);
    }
    B.at(M-d_NM) = i_C / A.at(N);
    debug_vec(B);
}

int main(){
    ll N, M;
    cin >> N >> M;
    vll A(N+1), B(M+1), C(N+M+1);
    rep(i, N+1) {
        cin >> A.at(i);
    }
    rep(i, N+M+1) {
        cin >> C.at(i);
    }
    debug_vec(A);
    debug_vec(C);

    B.at(M) = C.at(N+M) / A.at(N);
    for (size_t i = N+M-1; i>(N-1);i--) {
        waru(N, M, A, B, C, i);
    }
    for (size_t i=0;i<(M+1);i++) {
        cout << B.at(i);
        if (i != M) {
            cout << " ";
        }
    }
    cout << endl;
    return 0;
}

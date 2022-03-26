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

bool repeat_check(vll &A, vll &B, ll &N, ll &K, ll i, vll now_vals) {
    ll now_1 = now_vals.at(0);
    ll now_2 = now_vals.at(1);
    if (i == N) {
        return true;
    }
    ll next_A = A.at(i);
    ll next_B = B.at(i);

    i++;
    vll next_vals(2);

    if (now_1 != -1 && abs(now_1 - next_A) <= K) {
        next_vals.at(0) = next_A;
    } else if (now_2 != -1 && abs(now_2 - next_A) <= K) {
        next_vals.at(0) = next_A;
    } else {
        next_vals.at(0) = -1;
    }

    if (now_1 != -1 && abs(now_1 - next_B) <= K) {
        next_vals.at(1) = next_B;
    } else if (now_2 != -1 && abs(now_2 - next_B) <= K) {
        next_vals.at(1) = next_B;
    } else {
        next_vals.at(1) = -1;
    }

    if (next_vals.at(0) == -1 && next_vals.at(1) == -1) {
        return false;
    }

    return repeat_check(A, B, N, K, i, next_vals);
}

int main(){
    ll N, K;
    cin >>N >> K;
    vll A(N), B(N);
    vll now_vals(2);
    rep(i, N) {
        cin >> A.at(i);
    }
    rep(i, N) {
        cin >> B.at(i);
    }
    now_vals.at(0) = A.at(0);
    now_vals.at(1) = B.at(0);
    if (repeat_check(A, B, N, K, 1, now_vals)) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}

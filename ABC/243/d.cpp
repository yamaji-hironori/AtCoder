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

pair<ll, ll> process_U(ll X, ll stack_count) {
    if (stack_count > 0) {
        stack_count--;
    } else {
        X = X / 2;
    }
    return make_pair(X, stack_count);
}
pair<ll, ll> process_L(ll X, ll stack_count) {
    if (stack_count > 0) {
        stack_count++;
    } else {
        ll X_after = X * 2;
        if (X_after > pow(10, 18)){
            stack_count++;
            return make_pair(X, stack_count);
        } else {
            X = X_after;
        }
    }
    return make_pair(X, stack_count);
}
pair<ll, ll> process_R(ll X, ll stack_count) {
    if (stack_count > 0) {
        stack_count++;
    } else {
        ll X_after = (X * 2) + 1;
        if (X_after > pow(10, 18)){
            stack_count++;
            return make_pair(X, stack_count);
        } else {
            X = X_after;
        }
    }
    return make_pair(X, stack_count);
}

int main(){
    ll N, X;
    cin >> N >> X;
    string S;
    cin >> S;
    debug(N);
    debug(X);
    debug(S);
    ll stack_count = 0;
    for (ll i=0;i<N;i++) {
        if (S[i] == 'U') {
            tie(X, stack_count) = process_U(X, stack_count);
        } else if (S[i] == 'L') {
            tie(X, stack_count) = process_L(X, stack_count);
        } else {
            tie(X, stack_count) = process_R(X, stack_count);
        }
    }
    cout << X << endl;
    return 0;
}

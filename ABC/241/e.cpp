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
    ll N, K;
    cin>>N>>K;
    vector<ll> A(N);
    REP(i,N){
        cin>>A[i];
    }

    // パターンを見つける
    vector<ll> A_pattern(N);
    ll X_for_pattern = 0;
    ll before_loop_count = 0;
    ll before_loop_sum = 0;
    ll loop_count = 0;
    ll loop_sum = 0;
    ll loop_start_index = 0;
    while (true) {
        ll X_mod_N = X_for_pattern % N;
        if (A_pattern[X_mod_N] == 0) {
            A_pattern[X_mod_N] = 1;
            before_loop_count++;
            before_loop_sum += A[X_mod_N];
        } else if (A_pattern[X_mod_N] == 1) {
            A_pattern[X_mod_N] = 2;
            loop_count++;
            loop_sum += A[X_mod_N];
        } else if (A_pattern[X_mod_N] == 2) {
            A_pattern[X_mod_N] = 3;
            loop_start_index = X_mod_N;
            break;
        }
        X_for_pattern += A[X_mod_N];
    }

    ll X = 0;
    if (K <= before_loop_count) {
        for (ll i=0; i<K; i++) {
            ll X_mod_N = X % N;
            X += A[X_mod_N];
        }
    } else {
        ll K_in_loop = K - before_loop_count;
        ll all_loop = K_in_loop / loop_count;
        ll not_all_loop = K_in_loop % loop_count;
        X = before_loop_sum + (loop_sum*all_loop);
        for (ll i=0; i<not_all_loop; i++) {
            ll X_mod_N = X % N;
            X += A[X_mod_N];
        }
    }
    cout << X << endl;

    return 0;
}

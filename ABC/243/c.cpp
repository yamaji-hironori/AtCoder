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
    vector<ll> X(N);
    vector<ll> Y(N);
    for (ll i=0;i<N;i++){
        cin >> X[i] >> Y[i];
    }
    string S;
    cin >> S;

    map<ll, vector<ll> > Collision;
    //vector< vector<ll> > Collision(2, vector<ll>(pow(10, 9), -1));

    for (ll i=0;i<N;i++){
        if (Collision.count(Y[i]) == 0) {
            Collision[Y[i]].push_back(-1);
            Collision[Y[i]].push_back(-1);
        }

        if (S[i] == 'R') {
            if (Collision[Y[i]][0] == -1) {
                Collision[Y[i]][0] = X[i];
            } else if (Collision[Y[i]][0] > X[i]) {
                Collision[Y[i]][0] = X[i];
            }
        } else {
            if (Collision[Y[i]][1] == -1) {
                Collision[Y[i]][1] = X[i];
            } else if (Collision[Y[i]][1] < X[i]) {
                Collision[Y[i]][1] = X[i];
            }
        }
    }

    for (ll i=0;i<N;i++){
        if (Collision[Y[i]][0] == -1 || Collision[Y[i]][1] == -1) {
            continue;
        } else {
            if (Collision[Y[i]][0] < Collision[Y[i]][1]) {
                cout << "Yes" << endl;
                return 0;
            }
        }
    }

    cout << "No" << endl;
    return 0;
}

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
    ll H, W, N;
    ll start_x, start_y, goal_x, goal_y;
    cin >> H >> W >> N;
    cin >> start_x >> start_y >> goal_x >> goal_y;
    start_x--;start_y--;goal_x--;goal_y--;
    debug(H);
    debug(goal_y);
    vector< vector<int> > Skate(H, vector<int>(W));
    for (ll _=0;_<N;_++) {
        ll i_X, i_Y;
        cin >> i_X >> i_Y;
        i_X--;i_Y--;
        Skate.at(i_X).at(i_Y) = 1;
    }
    Skate.at(start_x).at(start_y) = 2;
    Skate.at(goal_x).at(goal_y) = 3;
    for (ll i = 0; i < H; i++) {
        for (ll j = 0; j < W; j++) {
            cout << Skate.at(i).at(j) << "; ";
        }
        cout << endl;
    }
    return 0;
}

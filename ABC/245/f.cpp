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
struct WalkRoute {
    ll from, to;
};
struct VertexStatus {
    int status = -1; // -1: 未計算, 0: 移動不可, 1: 移動可
    vll canGo; // 頂点から移動できる頂点群
};
int main(){
    ll N, M;
    cin >> N >> M;
    vector<WalkRoute> WalkRoutes(M);
    rep(i, M) {
        cin >> WalkRoutes.at(i).from >> WalkRoutes.at(i).to;
    }
    vector<VertexStatus> vertices(N+1);
    rep(i, M) {
        auto from_vertex = WalkRoutes.at(i).from;
        auto to_vertex = WalkRoutes.at(i).to;
        vertices.at(from_vertex).canGo.push_back(to_vertex);
    }

    cout << WalkRoutes.at(2).to << endl;
    return 0;
}

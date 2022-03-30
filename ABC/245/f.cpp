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
    int status = 0; // -1: 移動不可, 0: 未計算, 1: 移動可
    int aliveToRouteNum = 0;
    vll toRoute; // この頂点から行くことが出来る頂点群
    vll fromRoute; // この頂点へ行くことが出来る頂点群
};

void routeBack(vector<VertexStatus> &vertices, ll i_vertex_num) {
    if (vertices.at(i_vertex_num).aliveToRouteNum != 0) {
        return;
    }
    vertices.at(i_vertex_num).status = -1;
    for (ll i_fromRoute: vertices.at(i_vertex_num).fromRoute) {
        vertices.at(i_fromRoute).aliveToRouteNum--;
        routeBack(vertices, i_fromRoute);
    }
}

int main(){
    ll N, M;
    cin >> N >> M;
    vector<WalkRoute> WalkRoutes(M);
    rep(i, M) {
        cin >> WalkRoutes.at(i).from >> WalkRoutes.at(i).to;
    }
    vector<VertexStatus> vertices(N+1); // 頂点番号と要素番号を合わせるために１を加算する。
    rep(i, M) {
        auto from_vertex = WalkRoutes.at(i).from;
        auto to_vertex = WalkRoutes.at(i).to;
        vertices.at(to_vertex).fromRoute.push_back(from_vertex);
        vertices.at(from_vertex).toRoute.push_back(to_vertex);
    }
    for (size_t i=1;i<N+1;i++) {
        vertices.at(i).aliveToRouteNum = vertices.at(i).toRoute.size();
    }

    for (size_t i=1;i<N+1;i++) {
        if (vertices.at(i).toRoute.size() == 0) {
            if (vertices.at(i).fromRoute.size() == 0) {
                vertices.at(i).status = -1;
            } else {
                vertices.at(i).status = -1;
                for (ll i_fromRoute: vertices.at(i).fromRoute) {
                    vertices.at(i_fromRoute).aliveToRouteNum--;
                    routeBack(vertices, i_fromRoute);
                }
            }
        }
    }

    ll ans = 0;
    for (size_t i=1;i<N+1;i++) {
        if (vertices.at(i).status != -1) {
            ans++;
        }
    }
    cout << ans << endl;
    return 0;
}

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#ifdef _DEBUG
#define debug(x) cout<<#x<<": "<<x<<endl
#define debug_vec(x) for(size_t i=0;i<x.size();i++){cout<<x.at(i)<<"; ";}cout<<endl;
#define debug_vecvec(x) for(size_t i=0;i<x.size();i++){for(size_t j=0;j<x[i].size();j++){cout<<x.at(i).at(j)<<"; ";}cout<<endl;}cout<<endl;
#else
#define debug(x)
#define debug_vec(x)
#define debug_vecvec(x)
#endif

#define rep(i,n) for(size_t i=0;i<(n);++i)
int main(){
    int N, M;
    cin >> N >> M;
    vector<int> A(M), B(M);
    for (int i = 0; i < M; i++) {
        cin >> A.at(i) >> B.at(i);
    }
    vector< vector<char> > result(N, vector<char> (N, '-'));
    rep(i, M){
        result.at(A.at(i)-1).at(B.at(i)-1) = 'o';
        result.at(B.at(i)-1).at(A.at(i)-1) = 'x';
    }
    debug_vecvec(result);
    rep(i,N){
        rep(j,N){
            if (j == result.at(i).size()-1) {
                cout<<result.at(i).at(j)<<endl;
            } else {
                cout<<result.at(i).at(j)<<' ';
            }
        }
    }

    return 0;
}

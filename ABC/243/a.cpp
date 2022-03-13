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
    ll V, A, B, C;
    cin >> V >> A >> B >> C;
    while (true) {
        V -= A;
        if (V < 0) {
            cout << "F" << endl;
            return 0;
        }
        V -= B;
        if (V < 0) {
            cout << "M" << endl;
            return 0;
        }
        V -= C;
        if (V < 0) {
            cout << "T" << endl;
            return 0;
        }
    }
}

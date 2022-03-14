#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for(size_t i=0;i<(n);++i)
int main() {
    int N, A;
    cin >> N >> A;

    rep(i, N) {
        string op;
        int B;
        cin >> op >> B;
        if (op == "+") {
            A += B;
        } else if (op == "-") {
            A -= B;
        } else if (op == "*") {
            A *= B;
        } else {
            if (B==0) {
                cout<<"error"<<endl;
                return 0;
            }
            A /= B;
        }
        cout<<i+1<<":"<<A<<endl;
    }
}

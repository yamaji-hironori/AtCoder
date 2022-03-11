#include <bits/stdc++.h>
using namespace std;
int main(){
    int Q;
    cin >> Q;
    multiset<long long> A;
    for (int i = 0; i < Q; i++) {
        int query_type;
        cin >> query_type;
        if (query_type == 1) {
            long long x;
            cin >> x;
            A.insert(x);
        } else if (query_type == 2) {
            long long x;
            int k;
            bool break_flg = false;
            cin >> x >> k;
            auto iter = A.upper_bound(x);
            for (int i=0; i<k; i++) {
                if (A.begin() == iter) {
                    cout << "-1" << endl;
                    break_flg = true;
                    break;
                }
                iter--;
            }
            if (break_flg == false) {
                cout << *iter << endl;
            }
        } else if (query_type == 3) {
            long long x;
            int k;
            bool break_flg = false;
            cin >> x >> k;
            auto iter = A.lower_bound(x);
            for (int i=0; i<k-1; i++) {
                if (A.end() == iter) {
                    cout << "-1" << endl;
                    break_flg = true;
                    break;
                }
                iter++;
                if (A.end() == iter) {
                    cout << "-1" << endl;
                    break_flg = true;
                    break;
                }
            }
            if (break_flg == false && A.end() == iter) {
                cout << "-1" << endl;
                break_flg = true;
            }
            if (break_flg == false) {
                cout << *iter << endl;
            }
        }
    }

    return 0;
}

#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> data(5);
  for (int i = 0; i < 5; i++) {
    cin >> data.at(i);
  }

  int pre_data = data.at(0);
  for (int i=1;i<5;i++) {
    if (pre_data==data.at(i)) {
      cout<<"YES"<<endl;
      return 0;
    } else {
      pre_data = data.at(i);
    }
  }
  cout<<"NO"<<endl;
}

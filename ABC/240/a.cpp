#include <bits/stdc++.h>

using namespace std;

int main(){
  float A, B, C, X;
  cin >> A >> B >> C >> X;
  if (X <= A) {
    cout << 1 << endl;
  } else if (A < X && X <= B)
  {
    cout <<  C / (B-A) << endl;
  } else {
    cout << 0 << endl;
  }

  return 0;
}

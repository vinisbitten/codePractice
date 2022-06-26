#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;

  vector<int> arr(n);

  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }

  vector<int> pos(n + 1);

  for (int i = 1; i < n; i++) {
    pos[arr[i]] = i;
  }
  for (int i = 0; i < pos[n]; i++) {
    cout << endl;
  }
  cout << arr[pos[n]];
  int prv = pos[n];
  for (int i = n - 1; i > 0; i--) {
    if (pos[i] < prv) {
      cout << " " << arr[pos[i]];
    } else {
      int bfr = pos[i] - prv;
      while (bfr--) {
        cout << endl;
      }
      cout << arr[pos[i]];
      prv = pos[i];
    }
  }
  cout << endl;
  return 0;
}

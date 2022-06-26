#include <bits/stdc++.h>
#define MAX 200000

using namespace std;
using ll = long long;

int main()
{
    int n;
    ll x[MAX], m = 0;
    cin >> n;

    for(int i = 0; i < n; i++)
    {
        cin >> x[i];
    }

    ll result = x[0];

    for(int i = 0; i < n; i++)
    {
        m = max(x[i], m + x[i]);
        result = max(result, m);
    }
    cout << result << endl;
}

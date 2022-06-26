#include <bits/stdc++.h>

using namespace std;
using ll = long long;

int main()
{
    int n, div = 5, result = 0;
    cin >> n;

    while(n/div > 0)
    {
        result += n/div;
        div *= 5;
    }

    cout << result << endl;
}

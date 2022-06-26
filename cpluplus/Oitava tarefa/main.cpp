#include <bits/stdc++.h>
#define MAX 200000

using namespace std;
using ll = long long;

int main()
{
    ll n, aux;
    set<ll> x;

    cin >> n;

    for(int i = 0; i < n ; i++)
    {

        cin >> aux;
        x.insert(aux);
    }

    cout << x.size() << endl;
    return 0;
}

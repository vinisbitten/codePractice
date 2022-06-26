#include <bits/stdc++.h>
#define MAX 200000

using namespace std;

int main()
{
    int n, x;
    cin >> n >> x;

    map< int, int > mymap;
    for(int i = 0; i < n; i++)
    {
        int a;
        cin >> a;
        if(mymap.count(x - a))
        {
            cout << i+1 << " " << mymap[x - a] << endl;
            return 0;
        }
        mymap[a] = i + 1;
    }

    cout << "IMPOSSIBLE" << endl;
    return 0;
}

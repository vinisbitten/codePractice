#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    long long x[n];
    long long passos = 0;

    for(int i = 0; i < n; i++)
    {
        cin >> x[i];
        if(x[i] < x[i-1] && i >0){
            while(x[i] < x[i-1])
            {
                x[i] ++;
                passos ++;
            }
        }
    }
    cout << passos << endl;
    return 0;
}

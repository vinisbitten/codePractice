#include <bits/stdc++.h>

using namespace std;

int main()
{
    long long n;
    cin >> n;
    long long aux[n-1];
    long long soma = 0;

    for(long long i=0; i < n-1; i++)
    {
        cin >> aux[i];
        soma += aux[i];
    }

    long long resultado = n*(n+1)/2 - soma;

    cout << resultado << endl;

    return 0;
}

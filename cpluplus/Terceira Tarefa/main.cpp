#include <bits/stdc++.h>

using namespace std;

int main()
{
    string seq;
    long long rep = 1;
    long long maior = 1;
    cin >> seq;

    long long leng = seq.length()-1;

    for(int i = 0; i < leng;i++)
    {
        if(seq[i] == seq[i+1])
        {
            rep ++;
            if(rep > maior)
            {
            maior = rep;
            }
        }
        else
        {
            rep = 1;
        }
    }
    cout << maior << endl;

    return 0;
}

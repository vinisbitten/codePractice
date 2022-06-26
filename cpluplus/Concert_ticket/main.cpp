#include <bits/stdc++.h>
#define MAX 200000

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;

    int preco_tick[MAX];
    int max_preco[MAX];
    set < pair <int, int> > tickets;

    for(int i = 0; i < n; i++)
    {
        cin >> preco_tick[i];
        tickets.insert({preco_tick[i],i});
    }
    for(int i = 0; i < m; i++)
    {
        cin >> max_preco[i];
    }
    for(int i = 0; i < m; i++)
    {
        auto dale = tickets.lower_bound({max_preco[i]+1,0});
        if(dale == tickets.begin())
        {
            cout << -1 << endl;
        }
        else{
            dale --;
            cout << (*dale).first << endl;
            tickets.erase(dale);
        }
    }
    return 0;
}

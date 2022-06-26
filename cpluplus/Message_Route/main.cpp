#include <bits/stdc++.h>

using namespace std;

int n, m;
vector<vector<int>> grid;
vector<int> ordem;
vector<bool> vis;

void bfs()
{
    vis[1] = true;
    queue<int> q;
    q.push(1);
    while(!q.empty())
    {
        int a = q.front();
        q.pop();
        for(auto b: grid[a])
        {
            if(!vis[b])
            {
                vis[b] = true;
                ordem[b] = a;
                q.push(b);
            }
        }
    }
}

int main()
{
    cin >> n >> m;

    grid.resize(n+1);
    vis.resize(n+1);
    ordem.resize(n+1);

 	for(int i = 0; i<=n; ++i)
	{
		ordem[i] = -1;
	}
	for(int i = 0; i < m; ++i)
	{
		int a, b;
		cin >> a >> b;
		grid[a].push_back(b);
		grid[b].push_back(a);
	}
	bfs();

	if(ordem[n] == -1)
	{
		cout <<  "IMPOSSIBLE";
		return 0;
	}


	int candidate = n;
	stack<int> stk;
	while(candidate != -1)
	{
		stk.push(candidate);
		candidate = ordem[candidate];
	}

	cout << stk.size() << endl;

	while(!stk.empty())
	{
		cout << stk.top() << " ";
		stk.pop();
	}

    return 0;
}

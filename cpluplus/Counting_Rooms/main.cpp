#include <bits/stdc++.h>

using namespace std;
vector<vector<bool>> vis;
int n, m, salas;

bool valido(int x, int y)
{
    if(x<0 or x>=n or y<0 or y>=m)
        return false;
    if(vis[x][y])
        return false;
    return true;
}

void dfs(int i, int j)
{
    vector<pair<int,int>> mexe = {{-1,0}, {1,0}, {0,-1}, {0,1}};
    vis[i][j] = true;
    for(auto p: mexe)
    {
        if(valido(i+p.first, j+p.second))
        {
            dfs(i+p.first, j+p.second);
        }
    }
}

void pontos_conectados()
{
    for(int i=0; i<n; ++i)
    {
        for(int j=0; j<m; ++j)
        {
            if(!vis[i][j])
            {
                dfs(i, j);
                ++salas;
            }
        }
    }
}

int main()
{
    cin >> n >> m;
    vis.resize(n);

	for(int i = 0; i < n; ++i)
	{
		vis[i].resize(m);
	}

	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
		{
			char c; cin >> c;
			if(c == '#')
			{
				vis[i][j] = true;
			}
		}
	}
	pontos_conectados();
	cout << salas << endl;
}

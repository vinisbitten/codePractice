#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int t;
    cin >> t;

    while(t--)
    {
        string s;
        cin >> s;
        int tam = s.size();
        vector<int> arr;
        arr.push_back(0);

        for(int i = 0; i < tam; i++)
        {
            if(s[i] == 'R')
            {
                arr.push_back(i+1);
            }
        }
        arr.push_back(tam+1);

        int result = -1;

        for(int i = 1; i < arr.size(); i++)
        {
            result = max(result, arr[i]-arr[i-1]);
        }
        cout << result << endl;
    }
    return 0;
}

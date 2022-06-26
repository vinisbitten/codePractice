#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    long long arr [n];
    int aux = int(n/2);

    if(n == 2 || n == 3)
    {
        cout << "NO SOLUTION" << endl;
    }
    else
    {
        int i = 2;
        int j = 0;
        while(i < n/2)
        {
            cout << i << " ";
            j++;
            i += 2;
        }
    }


    return 0;
}

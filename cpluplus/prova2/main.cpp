#include <bits/stdc++.h>
#define MAX 100000

using namespace std;

int main()
{
    int n;
    cin >> n;
    int arr[MAX];
    for(int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    sort(arr, arr+n);

    cout << (n-1)/2 << endl;

    int new_arr[MAX], j = 0;

    for(int i = 1; i < n; i+=2, j++)
    {
        new_arr[i] = arr[j];
    }
    for(int i = 0; i < n; i +=2, j++)
    {
        new_arr[i] = arr[j];
    }

    for(int i = 0; i < n; i++)
    {
        cout << new_arr[i] << " ";
    }
    cout << endl;

    return 0;
}

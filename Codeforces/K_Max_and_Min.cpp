#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    int mn = a;
    if (b < mn) mn = b;
    if (c < mn) mn = c;

    int mx = a;
    if (b > mx) mx = b;
    if (c > mx) mx = c;

    cout << mn << " " << mx << endl;

    return 0;
}
// cout << min({a, b, c}) << " " << max({a, b, c}) << endl;
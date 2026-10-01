#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    int x = a, y = b, z = c;
    if (x > y) swap(x, y);
    if (y > z) swap(y, z);
    if (x > y) swap(x, y);
    cout << x << '\n' << y << '\n' << z << "\n\n";
    cout << a << '\n' << b << '\n' << c << '\n';
}
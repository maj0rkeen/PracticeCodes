#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    double x = (double)a / b;

    cout << "floor " << a << " / " << b << " = " << floor(x) << "\n";
    cout << "ceil " << a << " / " << b << " = " << ceil(x) << "\n";
    cout << "round " << a << " / " << b << " = " << round(x) << "\n";

    return 0;
}
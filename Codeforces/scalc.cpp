#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main(){
    int x,y;
    cin >> x >> y;
    cout << x << " + " << y << " = " << x + y << endl;
    cout << x << " * " << y << " = " <<(long long)x * y << endl; //typecast to long long to avoid overflow
    cout << x << " - " << y << " = " << x - y << endl;
}
#include <bits/stdc++.h>
using namespace std;
int main(){
    double x;
    cin >> x;
    string ans = "Interval ";

    if (x<0) 
        ans = "Out of Intervals";
    else if(x<=25)
        ans += "[0,25]";
    else if (x<=50)
        ans += "(25,50]";
    else if (x <=75)
        ans += "(50,75]";
    else if (x<=100)
        ans += "(75,100]";
    else 
        ans = "Out of Intervals";
    
        cout << ans <<endl;
}
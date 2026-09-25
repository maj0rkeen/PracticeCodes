#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    int years = n/365;
    n = n%365;
    int months = n/30;
    n %= 30;
    int days = n;
    cout <<  years << " years" << endl << months << " months" << endl << days << " days" << endl;
}
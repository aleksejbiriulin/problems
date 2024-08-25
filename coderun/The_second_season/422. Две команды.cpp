#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;


int main()
{
    int a, b, n, b1;
    cin >> a >> b >> n;
    b1 = b / n;
    if (b % n != 0){
        b1++;
    }
    if (a > b1){
        cout << "Yes";
    }else{
        cout << "No";
    }
    
    


    

    return 0;
}
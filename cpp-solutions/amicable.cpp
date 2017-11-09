#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

int d(int n){
    long int sum = 0;
    for(int i = 1; i < n; i++){
        if(n%i == 0){
            sum+=i;
        }
    }
    return sum;
}
int a(int lim) {
    int sum = 0;
    for(int i = 0; i < lim; i++){
        long int m = d(i);
        long int n = d(m);
        if (i == n && m != n){
            sum+=i;
        }
    }
    return sum;
}

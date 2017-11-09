/* 
 * File:   path.cpp
 * Author: Omochao
 *
 * Created on November 4, 2017, 2:45 PM
 */
using namespace std;
#include <cstdlib>
#include <iostream>
#include <fstream>
int path(int TN) {
    ifstream infile;
    //const int TN = 100;
    const int SIZE = (int)(TN*(TN+1))/2;
    int triangle[SIZE];
    int n;
    int t = 0;
    infile.open("C:\\Users\\Zyckr\\Documents\\NetBeansProjects\\Problems\\triangle.txt");
    while(infile >> n){
        triangle[t] = n;
        t++;
    }
    for(int i = TN-1; i > 0; i--){
        for(int j = (i*(i-1))/2; j < (i*(i+2))/2; j++){
            triangle[j] += max(triangle[j+i], triangle[j+i+1]);
        }
    }
    return triangle[0];
}


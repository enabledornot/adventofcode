#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int* toAry(string charStr) {
    int* elfpair = (int*)malloc(sizeof(int)*4);
    memset(elfpair,0,sizeof(int)*4);
    int currentNumb = 0;
    int cval = 0;
    for(int i = 0;i<charStr.length();i++) {
        if(charStr[i]=='-' || charStr[i]==',') {
            elfpair[currentNumb] = cval;
            currentNumb+=1;
            cval = 0;
        }
        else {
            cval*=10;
            cval+=charStr[i]-'0';
        }
    }
    elfpair[3] = cval;
    return elfpair;
}

bool isIntercept(string charStr) {
    int* EP = toAry(charStr);
    if(EP[1] < EP[2] || EP[0] > EP[3]) {
        return false;
    }
    free(EP);
    return true;
    
}

int main(int argc, char *argv[]) {
    ifstream input("input.txt");
    string fileText;
    int cnt = 0;
    while(getline(input, fileText)) {
        if(isIntercept(fileText)) cnt+=1;
    }
    cout << "Answer:";
    cout << cnt;
    cout << "\n";
}
#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

bool existsIn2ndHalf(char search, string sackString) {
    for(int i = sackString.length()/2;i<sackString.length();i++) {
        if(sackString[i]==search) {
            return true;
        }
    }
    return false;
}

char findCommonItem(string sackString) {
    for(int i = 0;i<sackString.length()/2;i++) {
        if(existsIn2ndHalf(sackString[i],sackString)) {
            return sackString[i];
        }
    }
    return '0';
}

int score(char charChar) {
    if(charChar <= 'Z') {
        return charChar - '@' + 26;
    }
    else {
        return charChar - '`';
    }
}

void addStrToArr(string current, int* intary, int level) {
    for(int i = 0;i<current.length();i++) {
        int cscore = score(current[i]);
        if(intary[cscore]==level) {
            intary[cscore]+=1;
        }
    }
}

int find3(int* intary) {
    for(int i = 0;i<55;i++) {
        if(intary[i]==3) {
            return i;
        }
    }
    return 0;
}

int main(int argc, char *argv[]) {
    ifstream input("input.txt");
    string fileText;
    int scoree = 0;
    int currentGroup[55];
    memset(currentGroup,0,55*sizeof(int));
    int cnt = 0;
    while(getline(input, fileText)) {
        addStrToArr(fileText, currentGroup, cnt%3);
        if(cnt%3==2) {
            scoree+=find3(currentGroup);
            memset(currentGroup,0,55*sizeof(int));
        }
        cnt+=1;
    }
    cout << "\n\nThe answer is:";
    cout << scoree;
    cout << "\n";
}
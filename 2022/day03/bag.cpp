#include <iostream>
#include <fstream>
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

int main(int argc, char *argv[]) {
    ifstream input("input.txt");
    string fileText;
    int scoree = 0;
    while(getline(input, fileText)) {
        if(fileText.length()!=0) {
            char common = findCommonItem(fileText);
            scoree+=score(common);
        }
    }
    cout << scoree;
    cout << "\n";
}
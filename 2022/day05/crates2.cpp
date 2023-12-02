#include <iostream>
#include <fstream>
#include <array>
#include <stack>
using namespace std;

void printAry(array<array<char,10>,10> ary) {
    for(int i = 0;i<sizeof(ary)/sizeof(ary[0]);i++) {
        for(int ii = 0;ii<sizeof(ary[0])/sizeof(ary[0][0]);ii++) {
            cout << ary[i][ii] << " ";
        }
        cout << "\n";
    }
}

array<int, 3> decodeArray(string input) {
    int current = 5;
    array<int, 3> rtn = {};
    rtn[0] = input[current]-'0';
    if(input[current+1]!=' ') {
        rtn[0]*=10;
        current+=1;
        rtn[0]+= input[current] - '0';
    }
    current+=7;
    rtn[1] = input[current]-'1';
    current+=5;
    rtn[2] = input[current]-'1';
    return rtn;
}

int main(int argc, char *argv[]) {
    ifstream input("input.txt");
    string fileText;
    int max = 0;
    int cnt = 0;
    array<array<char,10>,10> tmpBuffer = {};
    for(int i = 0;i<10;i++) {
        tmpBuffer[i] = {};
    }
    while(cnt<8) {
        getline(input, fileText);
        int ccount = 0;
        for(int i = 1;i<fileText.length();i+=4) {
            tmpBuffer[ccount][7-cnt] = fileText[i];
            ccount+=1;
        }
        cnt+=1;
    }
    printAry(tmpBuffer);
    stack<char> stacks[10];
    for(int i = 0;i<sizeof(stacks)/sizeof(stacks[0]);i++) {
        for(int ii = 0;ii<10;ii++) {
            if('A'<=tmpBuffer[i][ii] && tmpBuffer[i][ii]<='Z') {
                stacks[i].push(tmpBuffer[i][ii]);
            }
        }
    }
    getline(input, fileText);
    getline(input, fileText);
    while(getline(input, fileText)) {
        if(fileText.length()!=0) {
            array<int,3> decoded = decodeArray(fileText);
            stack<char> tmpStack = {};
            for(int i = 0;i<decoded[0];i++) {
                char tmp = stacks[decoded[1]].top();
                stacks[decoded[1]].pop();
                tmpStack.push(tmp);
            }
            for(int i = 0;i<decoded[0];i++) {
                char tmp = tmpStack.top();
                tmpStack.pop();
                stacks[decoded[2]].push(tmp);
            }
        }
    }

    cout << "Answer:";
    for(int i = 0;i<10;i++) {
        if(!stacks[i].empty()) {
            cout << stacks[i].top();
        }
    }
    cout << "\n";
}
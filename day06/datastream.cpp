#include <iostream>
#include <fstream>
using namespace std;

bool containsDupe(int start, string fileString) {
    for(int i = start;i<4+start;i++) {
        for(int ii = start;ii<4+start;ii++) {
            if(i!=ii && fileString[i]==fileString[ii]) {
                return true;
            }
        }
    }
    return false;
}

int main(int argc, char *argv[]) {
    ifstream input("input.txt");
    string fileText;
    getline(input, fileText);
    for(int i = 0;i<fileText.length()-4;i++) {
        if(!containsDupe(i,fileText)) {
            cout << "Answer:";
            cout << i+4;
            cout << "\n";
            for(int k = i;k<i+4;k++) {
                cout << fileText[k];
            }
            cout << "\n";
            break;
        }
    }
}
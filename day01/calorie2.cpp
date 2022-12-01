#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int main(int argc, char *argv[]) {
    ifstream input("input.txt");
    string fileText;
    int cnt = 0;
    int max[3];
    memset(&max, 0, sizeof(int)*3);
    while(getline(input, fileText)) {
        if(fileText.length()==0) {
            int i = 0;
            while(i<3 && max[i]>cnt) {
                i = i + 1;
            }
            int prev;
            if(i<3) {
                prev = max[i];
                max[i] = cnt;
                i = i + 1;
            }
            while(i<3) {
                int swap = max[i];
                max[i] = prev;
                prev = swap;
                i = i + 1;
            }
            cnt = 0;
        }
        else {
            cnt+=stoi(fileText);
        }
    }
    cout << "Answer:";
    int sum;
    for(int i = 0;i<3;i++) {
        sum+=max[i];
    }
    cout << sum;
    cout << "\n";
}
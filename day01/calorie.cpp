#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]) {
    ifstream input("input.txt");
    string fileText;
    int cnt = 0;
    int max = 0;
    while(getline(input, fileText)) {
        if(fileText.length()==0) {
            if(max<cnt) {
                max = cnt;
            }
            cnt = 0;
        }
        else {
            cnt+=stoi(fileText);
        }
    }
    cout << "Answer:";
    cout << max;
    cout << "\n";
}
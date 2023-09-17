#include <iostream>
#include <fstream>
#include <list>
#include <cstring>
using namespace std;
class CPU {
    public:
        int cycleCount;
        CPU() {
            X = 2;
            clock = 0;
            cycleCount = 0;
        }
        void exec(string inst) {
            if(inst.starts_with("noop")) {
                cycle();
            }
            else {
                cycle();
                cycle();
                int val = stoi(inst.substr(5));
                X+=val;
            }
        }
        void cycle() {
            clock+=1;
            if(abs(clock%40-X)<2) {
                cout << "█";
            }
            else {
                cout << " ";
            }
            if(clock%40==0) {
                cout << "\n";
            }
        }
    private:
        int X;
        int clock;
};
int main(int argc, char *argv[]) {
    ifstream input("input.txt");
    string fileText;
    int cnt = 0;
    CPU c = CPU();
    while(getline(input, fileText)) {
        c.exec(fileText);
        cnt+=1;
    }
}
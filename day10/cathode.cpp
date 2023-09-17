#include <iostream>
#include <fstream>
#include <list>
#include <cstring>
using namespace std;
class CPU {
    public:
        int cycleCount;
        CPU(list<int> pl) {
            X = 1;
            clock = 0;
            printList = pl;
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
    private:
        int X;
        int clock;
        list<int> printList;
        void cycle() {
            clock+=1;
            if(find(printList.begin(),printList.end(),clock) != printList.end()) {
                cycleCount+=X*clock;
            }
        }
};
int main(int argc, char *argv[]) {
    ifstream input("input.txt");
    string fileText;
    int cnt = 0;
    list<int> printCycles = {20,60,100,140,180,220};
    CPU c = CPU(printCycles);
    while(getline(input, fileText)) {
        c.exec(fileText);
        cnt+=1;
    }
    cout << c.cycleCount;
    cout << "\n";
}
#include <iostream>
#include <fstream>
using namespace std;

typedef struct gamePlay {
    int elfmove;
    int mymove;
} gp;

//A X - Rock
//B Y - Paper
//C Z - Scissors



gp getCodedScore(string line) {
    gp gameplay;
    switch(line[0]) {
        case 'A':
            gameplay.elfmove = 1;
            break;
        case 'B':
            gameplay.elfmove = 2;
            break;
        case 'C':
            gameplay.elfmove = 3;
            break;
    }
    switch(line[2]) {
        case 'X':
            gameplay.mymove = 1;
            break;
        case 'Y':
            gameplay.mymove = 2;
            break;
        case 'Z':
            gameplay.mymove = 3;
            break;
    }
}

int main(int argc, char *argv[]) {
    ifstream input("input.txt");
    string fileText;
    int myScore = 0;
    while(getline(input, fileText)) {
        if(fileText.length()!=0) {
            myScore+=calculateScore(fileText);
        }
    }
}
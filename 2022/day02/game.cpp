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
    return gameplay;
}

int calculateScore(string fileText) {
    gp gamePlay = getCodedScore(fileText);
    if(gamePlay.mymove == gamePlay.elfmove) {
        return gamePlay.mymove + 3;
    }
    else if(gamePlay.elfmove == 3 && gamePlay.mymove == 1) {
        return gamePlay.mymove + 6;
    }
    else if(gamePlay.elfmove == 1 && gamePlay.mymove == 3) {
        return gamePlay.mymove;
    }
    else if(gamePlay.mymove > gamePlay.elfmove) {
        return gamePlay.mymove + 6;
    }
    else {
        return gamePlay.mymove;
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
    cout << "The answer is:";
    cout << myScore;
    cout << "\n";
}
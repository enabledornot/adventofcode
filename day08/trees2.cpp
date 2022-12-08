#include <iostream>
#include <fstream>
#include <list>
#include <cstring>
using namespace std;


int locateTree(int* treeAry, int posx, int posy) {
    return treeAry[99*posx+posy];
}

int checkDirection(int* treeAry, int posx, int posy, int dirx, int diry) {
    int prev = locateTree(treeAry, posx, posy);
    int cnt = 0;
    while(posx!=0 && posx!=99-1 && posy!=0 && posy!=99-1) {
        posx+=dirx;
        posy+=diry;
        int newt = locateTree(treeAry, posx, posy);
        if(newt>=prev) {
            return cnt+1;
        }
        cnt+=1;
    }
    return cnt;
}

int checkSurrounding(int* treeAry, int posx, int posy) {
    int currentTree = locateTree(treeAry,posx,posy);
    // cout << currentTree;
    if(posx==0 || posx==99-1 || posy==0 || posy==99-1) {
        return 0;
    }
    int startingScore = 1;
    startingScore*=checkDirection(treeAry,posx,posy,1,0);
    startingScore*=checkDirection(treeAry,posx,posy,-1,0);
    startingScore*=checkDirection(treeAry,posx,posy,0,1);
    startingScore*=checkDirection(treeAry,posx,posy,0,-1);
    return startingScore;
}

int main(int argc, char *argv[]) {
    ifstream input("input.txt");
    string fileText;
    int treeAry[99][99];
    memset(&treeAry,0,sizeof(int)*99*99);
    int cnt = 0;
    while(getline(input, fileText)) {
        for(int i = 0;i<99;i++) {
            treeAry[cnt][i] = fileText[i]-'0';
        }
        cnt+=1;
    }
    int ans = 0;
    int max = 0;
    for(int i = 0;i<99;i++) {
        for(int ii = 0;ii<99;ii++) {
            int rslt = checkSurrounding(*treeAry,i,ii);
            if(rslt>max) {
                max = rslt;
            }
            cout << "(" << treeAry[i][ii] << "," << rslt << ")";
        }
        cout << "\n";
    }
    cout << "Answer:";
    cout << max;
    cout << "\n";
}
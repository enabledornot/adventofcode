#include <iostream>
#include <fstream>
#include <cstring>
#include <list>
#define X 41
#define Y 64
using namespace std;

class node {
    public:
        int x;
        int y;
};
void printAry(int* ary) {
    for(int i = 0;i<X;i++) {
        for(int ii = 0;ii<Y;ii++) {
            if(ary[i*Y + ii]/10==0) {
                cout << ary[i*Y + ii] << " ";
            }
            else {
                cout << ary[i*Y + ii];
            }
            cout << " ";
        }
        cout << "\n";
    }
}

bool isValid(int start[2], int move[2], int* hightMap, int* distMap) {
    if(move[0]<0) return false;
    if(move[1]<0) return false;
    if(move[0]>=X) return false;
    if(move[1]>=Y) return false;
    if(distMap[move[0]*Y + move[1]] != -1) return false;
    if(hightMap[move[0]*Y + move[1]]-hightMap[start[0]*Y + start[1]] > 1) return false;
    return true;
}

int getDistTo(int start[2], int end[2], int* hightMap, int* distMap) {
    memset(distMap, -1, sizeof(int)*X*Y);
    distMap[start[0]*Y + start[1]] = 0;
    list<int*> processList;
    int directions[4][2] = {{0,-1},{-1,0},{0,1},{1,0}};
    int* tmp = (int*)malloc(sizeof(int)*2);
    tmp[0] = start[0];
    tmp[1] = start[1];
    processList.push_back(tmp);
    while(true) {
        if(processList.empty()) break;
        int* starting = processList.front();
        processList.pop_front();
        for(int i = 0;i<4;i++) {
            int* newMove = (int*)malloc(sizeof(int)*2);
            newMove[0] = starting[0] + directions[i][0];
            newMove[1] = starting[1] + directions[i][1];
            if(isValid(starting, newMove, hightMap, distMap)) {
                processList.push_back(newMove);
                distMap[newMove[0]*Y + newMove[1]] = distMap[starting[0]*Y + starting[1]] + 1;
                if(newMove[0]==end[0] && newMove[1]==end[1]) {
                    return distMap[starting[0]*Y + starting[1]] + 1;
                }
            }
            else {
                free(newMove);
            }
        }
        free(starting);
    }
    return 2000000;
}

int main(int argc, char *argv[]) {
    ifstream input("input.txt");
    string fileText;
    int hightMap[X][Y];
    int distMap[X][Y];
    int start[2];
    int end[2];
    memset(&hightMap, -1, sizeof(int)*X*Y);
    int i = 0;
    list<int*> aList;
    while(getline(input, fileText)) {
        for(int ii = 0;ii<fileText.length();ii++) {
            if('a' <= fileText[ii] && fileText[ii] <= 'z') {
                hightMap[i][ii] = fileText[ii]-'a';
            }
            else if(fileText[ii]=='S') {
                start[0] = i;
                start[1] = ii;
            }
            else {
                end[0] = i;
                end[1] = ii;
                hightMap[i][ii] = 26;
            }
            if('a' == fileText[ii]) {
                int* tmp = (int*)malloc(sizeof(int)*2);
                tmp[0] = i;
                tmp[1] = ii;
                aList.push_back(tmp);
            }
        }
        i+=1;
    }
    int min = 50000;
    while(!aList.empty()) {
        int* toProcess = aList.front();
        int rslt = getDistTo(toProcess, end, *hightMap, *distMap);
        aList.pop_front();
        if(rslt < min) {
            min = rslt;
        }
    }
    cout << "Answer:";
    cout << min;
    cout << "\n";
}
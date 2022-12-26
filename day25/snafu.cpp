#include <iostream>
#include <fstream>
using namespace std;

long snafutoint(string snafu) {
    long num = 0;
    for(int i = 0;i<snafu.length();i++) {
        switch(snafu[i]) {
            case '=':
            num-=2;
            break;

            case '-':
            num-=1;
            break;

            case '1':
            num+=1;
            break;

            case '2':
            num+=2;
            break;
        }
        num*=5;
    }
    return num/5;
}

string inttosnafu(long num) {
    string snafu = "";
    while(num!=0) {
        switch(num%5) {
            case 4:
            num+=1;
            snafu = "-" + snafu;
            break;

            case 3:
            num+=2;
            snafu = "=" + snafu;
            break;

            case 2:
            num-=2;
            snafu = "2" + snafu;
            break;

            case 1:
            num-=1;
            snafu = "1" + snafu;
            break;

            case 0:
            snafu = "0" + snafu;
            break;
        }
        num = num/5;
    }
    return snafu;
}

int main(int argc, char *argv[]) {
    ifstream input("input.txt");
    string fileText;
    long cnt = 0;
    while(getline(input, fileText)) {
        cnt+=snafutoint(fileText);
    }
    cout << cnt;
    cout << "\n";
    cout << "Answer:";
    cout << inttosnafu(cnt);
    cout << "\n";
}
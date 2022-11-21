#include <iostream>
using namespace std;

void test()
{
    int curVal = 0, val = 0;
    dd;
    
    if (cin >> curVal){
        int cnt = 1;
        while(cin >> val){
            if (val == curVal)
                ++ cnt;
            else{
                cout << curVal << "occurs" << cnt << "times" << endl;
                curVal = val;
                cnt = 1;
            }
        }
        cout << curVal << "occurs" << cnt << "times" << endl;
    }

}


int main()
{   
    test();
    return 0;
}

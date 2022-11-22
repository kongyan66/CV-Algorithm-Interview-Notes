#include <iostream>
using namespace std;

void test()
{
    int a = 0, b = 1;
    int *p1 = &a, *p2 = p1;
    cout << *p2 << endl;
    *p2 = b;
    cout << *p2 << endl;
}


int main()
{   
    test();
    return 0;
}

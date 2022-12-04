#include "chapter6.h"
using namespace std;

int test24(int val)
{
  if(val < 0)
  {
    return -1;
  }
  int res = 1;
  for (int i = 1; i != val + 1; ++i)
  {
    res *= i;
  }
  return res;
}


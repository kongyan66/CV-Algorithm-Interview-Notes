#include <iostream>
#include <string>

using namespace std;

void test1()
{
  
  string s("Hello World!!!");
  cout << s.size() << endl;
  decltype(s.size()) punct_cnt = 0;

  for  (auto c : s)
  if (ispunct(c))
    ++punct_cnt;
  cout << punct_cnt << endl;
  
  string orig = s;
  for (auto &c : s)
    c = toupper(c);
  cout << s << endl;
  s = orig;
  decltype(s.size()) index = 0;
  while (index != s.size() && !isspace(s[index]))
  {
    s[index] = toupper(s[index]);
    ++index;
  }

  cout << s << endl;
}

void test2()
{
  string s1, s2;
  cin >> s1 >> s2;
  if (s1.size() == s2.size())
    cout << "the two strings are equal" << endl;   
  else
    cout << "The larger string is " << ((s1.size() > s2.size()) ? s1: s2) << endl;

}

void test3()
{
  string result, s;
  char cont('y');
  while (cin >> s)
  {
    result += s + ' ';
    cout << "是否继续(y or n)?" << endl;
    cin >> cont; 
    if (cont == 'y' || cont == 'Y')
      cout << "请输入下一个字符串" << endl;
    else
      break;
  }
  
  cout << result << endl;
}

void test4()
{
  string s("this ");
  cout << s.size() << endl;
  for (char &x : s)
    x = 'X';
  cout << s << endl;
}

void test5()
{
  string s = "this ";
  int i = 0;
  while (i != s.size())
  {
    s[i] = 'X';
    ++i;
  }
  cout << s << endl;
}

int main()
{
  test4();
  return 0;
}
#include"iostream"
#include <string>
#include <vector>
#include <typeinfo>
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

void test6()
{
  vector<int> text = {1, 2, 3, 4, 5};
  auto sought = 2;
  auto beg = text.begin(), end = text.end();
  auto mid = beg + (end - beg) / 2;

  while (mid != end && *mid != sought)
  {
    if (sought < *mid)
      end = mid;
    else
      beg = mid;
    mid = beg + (end - beg) / 2;
  }
  if(mid !=text.end())
    cout << "找到了 "<< *mid << endl;
  else
    cout << "没有找到" << endl;
}

void test7()
{
  vector<string> v;
  string s;
  while(cin >> s)
  {
    v.push_back(s);
  
  }

  for (auto i : v)
  {
    cout << i << " ";
  }
  cout << endl;
}

void test8()
{
  vector<string> v;
  string s;

  while(cin >> s)
    v.push_back(s);

  for (auto &m : v)
  {
    for (auto &n : m)
    {
      n = toupper(n);
    }
  }

  for(auto i : v)
    cout << i << endl;
}

void test9()
{
  vector<int> v;
  int i;

  while(cin >> i)
  {
    v.push_back(i);
  }
  for(int i = 0; i < v.size(); ++i)
  {
    cout << v[i] + v[i - 1] << endl;
  }
  cout << "---------------------------------" << endl;
  int m = 0;
  int n = v.size() - 1;
  while(m < n){
    cout << v[m] + v[n] << endl;
    ++ m;
    --n;
  }
}

void test10()
{
  vector<int> v;
  int i;

  while(cin >> i){
    v.push_back(i);
  }

  for(auto it = v.begin(); it < v.end(); ++it)
     cout << *it + *(it + 1) << endl;

}

bool test11(int* const pb1, int* const pe1, int* const pb2, int* const pe2)   
{
  if (pe1 - pb1 != pe2 - pb2) return false;
  else
  {
    for (auto pt1 = pb1, pt2 = pb2; (pt1 != pe1) && (pt2 != pe2); ++pt1, ++pt2){
      if (*pt1 != *pt2) return false;
    }
  }
  return true;
}

void test12()
{
 int arr[3][4] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
//  for (int (&row)[4] : arr){
//   for (int (&col) : row){
//     cout << col << " ";
//   }
//   cout << endl;

  // for (int(*row)[4] = arr; row != arr + 3; ++row){
  //   for (int *col = *row; col != *row + 4; ++col){
  //       cout << *col << " ";
  //   } 
  //   cout << endl;
  for (auto &row : arr){
    for (auto col : row){
      //cout << typeid(col).name() << " ";
      cout << col << " ";
    }
    cout << endl;
  }
  }
  
  void test13()
  {
    vector<int> v = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    for (auto &i : v)
    {
      cout << ((i % 2 != 0) ? i * 2 : i) << " ";
    }
    cout << endl;
  }

  void test14()
  {
    for (unsigned g; cin >> g;)
    {
      string result = g > 90 ? "high pass" : g > 75 ? "pass" : g > 60 ? "low pass" : "fail";
      cout << result << endl;
    }
  }
  
void test15()
{
  int x[10]; int *p = x;
  cout << sizeof(x) / sizeof(*x) << endl;
  cout << sizeof(p) << endl;
}
void test16()
{
  switch(2){
    case 1:
      {int b = 0;}
      int c;
      break;
    case 2:
      cout << "before c = " << c << endl;
      c = 1;
      int a = 1;
      cout << "after c = " << c << endl;
      // break;
  }
}

void test17()
{
  vector<string> scores = { "F", "D", "C", "B", "A", "A++" };
  for(int g; cin >> g;)
  {
    string letter;
    if (g < 60)
    {
      letter = scores[0];
    }
    else 
    {
      letter = scores[(g - 50) / 10];
      if (g != 100)
      {
        letter += g % 10 > 7 ? "+" : g % 10 < 3 ? "-" : "";
      }
    }
    cout << letter << endl;
  }
}

void test18()
{
  string pre, cur = "", maxString;
  int curCnt = 1, maxCnt = 0;
  while (cin >> pre)
  {
    if(pre == cur)
    {
      ++curCnt;
      if(curCnt > maxCnt){
        maxCnt = curCnt;
        maxString = cur;
      }
    }
    else{
      curCnt = 1;
    }
    cur = pre;
  }
  if(maxCnt > 1)
  {
    cout << "出现最多的字符是："<< maxString << "出现了次数为:" << maxCnt <<endl;
  }
  else
    cout << "每个字符串只出现了一次" << endl;
}

void test19()
{
  vector<int> v1 = {0, 1, 2};
  vector<int> v2 = {0, 1};
  auto it1 = v1.begin();
  auto it2 = v2.begin();

  while(it1 != v1.end() && it2 != v2.end())
  {
    if (*it1 != *it2){
      cout << "v1和v2之间不存在前缀关系" << endl;
      break;
    }
    ++it1;
    ++it2;

    if (it1 == v1.end())
    {
      cout << "v1是v2的前缀" << endl;
    }
    if (it2 == v2.end())
    {
      cout << "v2是v1的前缀" << endl;
    }

  }
}

void test20()
{
  do{
    string str1, str2;
    cin >> str1 >> str2;
    (str1.size() > str2.size()) ? cout << "str2 短些" << endl : cout << "str1短些" << endl;
  }
  while(cin);
}

void test21()
{
  string cur, pre = "";
  bool no_twice = true;
  while(cin >> cur)
  {
    if(isupper(cur[0]) && cur == pre)
    {
      cout << "occurs twice in succession" << endl;
      no_twice = false;
      break;
    }
    pre = cur;
  }

  if(no_twice)
  {
    cout << "no word was repeated." << endl;
  }
}

void test22()
{
  for(int i, j; cin >> i >>j;)
  {
  try
  {
    if (j == 0)
    {
    throw runtime_error("divsor is zero");
    }
    cout << i / j << endl;
  }
  catch(runtime_error err)
  {
    cout << err.what() << "\nTry again? Enter y or n" << endl;
    char c;
    cin >> c;
    if(!cin || c == 'n')
      break;
  }
  }
}

void test23(int *ip)
{
  *ip = 0;
  ip = 0;
}



int main()
{
  int i = 42;
  cout << &i << endl;
  test23(&i);
  cout << &i << endl;
  cout << "i=" << i << endl;
  return 0;
}
#include"iostream"
#include <string>
#include <vector>
#include <typeinfo>
#include <cassert>
#include <fstream>
#include <deque>
#include <list>
#include <forward_list>
#include <algorithm>
#include <numeric>
#include <functional>
#include <iterator>
#include <map>
#include <sstream>
using namespace std;
using namespace std::placeholders;

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

void test25(int p, int q)
{
  int tem = p;
  p = q;
  q = tem;
}

void test26(int &i)
{
  i = 0;
}

string::size_type test27(const string &s, char c, const int &occurs)
{
  auto ret = s.size();
  // occurs = 0;
  for (decltype(ret) i = 0; i != s.size(); ++i)
  {
    if(s[i] == c)
    {
      if(ret == s.size())
      {
        ret = i;
      }
      //++occurs;
    }
  }
  return ret;
}

int &test27(int *arry, int index)
{
 return arry[index];
}

void test28(vector<int> vInt, unsigned index)
{
  unsigned sz = vInt.size();
  #ifdef DEBUG
 
    cout << "nihao" << endl;
  #endif
  if(!vInt.empty() && index < sz)
  {
    cout << vInt[index] << endl;
    test28(vInt, index + 1);
  } 
}

void test29()
{
  cout << "该函数无需参数" << endl;
}
void test29(int)
{
  cout << "该函数需要一个int参数" << endl;
}
void test29(int, int)
{
  cout << "该函数需要两个int参数" << endl;
}
void test29(double, double = 3.14)
{
  cout << "该函数需要两个浮点数" << endl;
}

int test30(int a, int b)
{
  cout << a << endl;
  cout << b << endl;
  return 1;
}

int add(int a, int b)
{
  return a + b;
}

int sub(int a, int b)
{
  return a - b;
}

// void test30()
// {
//   Sales_data total;
//   if(cin >> total.bookNo >> total.units_sold >> total.revenue)
//   {
//     Sales_data trans;
//     while(cin >> trans.bookNo >> trans.units_sold >> trans.revenue)
//     {
//       if (total.bookNo == trans.bookNo)
//       {
//         total.units_sold += trans.units_sold;
//         total.revenue ++ trans.revenue;
//       }
//       else
//       {
//         cout << total << endl;
//         total = trans;
//       }
//     }
//     cout << total << endl;
//   }
//   else
//   {
//     cerr << "NO DATA" << endl;
//     return -1;
//   }
//   return 0;
// }

// void test31()
// {
//   class Sales_data
//   {
//     private:
//       string booNo;
//       unsigned units_sold = 0;
//     public:
//       // 定义isbn()函数
//       string isbn() const 
//       {
//         return bookNo;
//       }
//       // 定义combin函数
//       Sales_data& combine(const Sales_data &rhs)
//       {
//         units_sold += rhs.units_sold;
//         return *this;
//       }

//   }
// }

// void test32()
// {
//   class Person
//   {
//     friend istream &read(istream &is, Person &item);
//     friend ostream &print(ostream &os, const Person &rhs);
//     private:
//       string name;
//       string address;
//     public:
//       Person() = default;
//       Person(const string &name_, const string &add_):name(name_), address(add_) {}
//       Person(istream &is) {read(is, *this);}
//     public:
//       string getName() const { return name;}  // 定义为
//       string getAddress() const { return address;}
    

//   };
//   istream &read(istream &is, Person &person)
//   {
//     return is >> person.name >> person.address;
//   }
//   ostream &print(ostream &os, const Person &person)
//   {
//     return os << person.name << " " << person.address;
//   }

// }
// void test33()
// {
// class Sales_data
// {
//   public:
//     Sales_data() = default;
//     Sales_data(const string &book) : bookNo(book) {}
//     Sales_data(const string &book, const unsigned num,
//       const double sellp, const double salep);
//     Sales_data(std::istream &is);
//   public:
//     string bookNo;
//     unsigned units_sold = 0;
//     double sellingprice = 0.0;
//     double saleprice = 0.0;
//     double discount = 0.0;
// };

//   Sales_data data1;
//   Sales_data data2("90-998-1");
//   Sales_data data3("887-99", 100, 128, 109);
//   cout << data1 << endl;

// }

// void test34()
// {
//   class Screen{
//     public:
//       typedef string::size_type pos;
//       // 构造函数
//       Screen() = default;
//       // Screen(pos ht, pos wd, char c) : height(ht), width(wd), contents(ht * wd, ' ') { }
//       Screen(pos ht, pos wd, char c) : height(ht), width(wd), contents(ht * wd, c) { }
//       // 成员函数
//       char get() const {return contents[cursor];}
//       char get(pos r, pos c) const {return contents[r * width + c];}
//       void display(ostream &os) const {os << contents << endl;}
//       void move(pos r, pos c)  {cursor = r * width + c;}
//       void set(char ch) {contents[cursor] = ch;}
//     public:
//       pos cursor = 0;
//       pos height = 0, width = 1;
//       string contents;
//   };

//   Screen myscreen(3, 3, 'X');
//   myscreen.move(12, 0);
//   cout << myscreen.cursor << endl;
//   myscreen.set('*');
//   myscreen.display(cout);

// }

// void test35()
// {
//   class Book
//   {
//     private:
//       string Name, ISBN, Author, publisher;
//       double Price = 0;
//     public:
//       Book(const string n):Name(n) {}
//       Book(istream &is) {is >> *this;}
//       void print(){cout << Name << endl;}

//   };

//   Book book(cin);
//   book.print();
// }

int test36()
{
  ifstream in("test.txt");
  if (!in){
    cerr << "无法打开输入文件" << endl;
    return -1;
  }
  string line;
  vector<string> words;
  while(in >> line)
  {
    words.push_back(line);
  }
  in.close();
  auto it = words.begin();
  while(it != words.end())
  {
    cout << *it << endl;
    ++it;
  }
  return 0;
}
vector<int>::const_iterator test37(vector<int>::const_iterator begin, vector<int>::const_iterator end, int i)
{
  while(begin != end)
  {
    if(*begin == i)
    {
      return begin;
    }
    ++begin;
  }
  return end;
}

void test38()
{
  list<string> input;
  for(string str; cin >> str; input.push_back(str));
  for(auto iter = input.cbegin(); iter != input.cend(); ++iter)
    cout << *iter << endl;
}

void test39()
{
  list<int> l{1, 2, 3, 4, 5, 6, 7, 8, 9};
  deque<int> odd, even;
  for(auto i : l)
  {
    (i % 2 ? odd : even).push_back(i);
  }
  for(auto i : odd) cout << i << " ";
  cout << endl;
  for(auto i : even) cout << i << " ";
  cout << endl;
}

void test40()
{
  vector<int> iv{1, 2};
  cout << iv.at(0) << endl;
  cout << iv[0] << endl;
  cout << iv.front() << endl;
  cout << *(iv.begin()) << endl;
}

void test41()
{
  int a[] = { 0, 1, 1, 2, 3, 5, 8, 13, 21, 55, 89 };
  vector<int> vec(begin(a), end(a));
  list<int> lst(begin(a), end(a));
  for (auto it = lst.begin(); it != lst.end();)
  {
    if (*it & 0x1)
    {
      it = lst.erase(it);
    }
    else
      ++it;
  }
  for (auto it = vec.begin(); it != vec.end();)
  {
    if (!(*it & 0x1))
    {
      it = vec.erase(it);
    }
    else
      ++it;
  }

  for(auto i:lst){
    cout << i << " ";
  }
  cout << endl;
  for(auto i:vec){
  cout << i << " ";
  }
  cout << endl;
 
}

void test42()
{
  forward_list<int> iflst = {1, 2, 3, 4, 5, 6, 7, 8};
  auto pre = iflst.before_begin();
  auto cur = iflst.begin();

  while(cur != iflst.end())
  {
    if (*cur & 0x1)
    {
      cur = iflst.erase_after(pre);
    }
    else
    {
      pre = cur;
      ++cur;
    }
  }
  for(auto v : iflst)
  {
    cout << v << " ";
  }
  cout << endl;
}
void test43()
{
  vector<int> v;
  for(int i = 0; i < 10; i++)
  {
    cout << "capactity: " << v.capacity() << "  size: " << v.size() << endl;
    v.push_back(i);
    
  }
}

void test44()
{
  vector<int> v = {1, 2, 3, 4, 5, 6, 6, 6, 2};
  cout << count(v.cbegin(), v.cend(), 6) << endl;

  list<string> l = {"aa", "aaa", "aa", "cc"};
  cout << count(l.cbegin(), l.cend(), "aa") << endl;
}

void test45()
{
  vector<double> v = {1.1, 2.1, 3.1};
  cout << accumulate(v.cbegin(), v.cend(), 0) << endl;
}

void output_words(vector<string> &words)
{
  for(auto iter = words.begin(); iter != words.end(); iter++)
  {
    cout << *iter << " ";
  }
  cout << endl;
}

void test46(vector<string> &words)
{
  output_words(words);
  sort(words.begin(), words.end());
  output_words(words);

  auto end_unique = unique(words.begin(), words.end());
  output_words(words);

  words.erase(end_unique, words.end());
  output_words(words);

}

bool is_shorter(const string &s1, const string &s2)
{
  return s1.size() < s2.size();
}

void add(int a)
{
  auto sum = [a] (int b) {return a + b;};
  cout << sum(1) << endl;
}

void test47()
{
  int i = 5;
  auto f = [i] () mutable -> bool {if(i > 0){i--; return false;} else return true;};
  for(int j = 0; j < 6; j++)
    cout << f() << " ";
  cout << endl;
}

bool check_size(const string &s, string::size_type sz)
{
  return s.size() <= sz;
}

void test48(vector<int> &vc, const string &s)
{
  auto p = find_if(vc.begin(), vc.end(), bind(check_size, s, _1));
  cout << "第" << p - vc.begin() + 1 << "个数" << *p << "大于等于" << s << "的长度" << endl;
}

void test49()
{
  vector<int> vc{1, 1, 3, 3, 4};
  list<int> ls;

  unique_copy(vc.begin(), vc.end(), back_inserter(ls));
  for(auto i : ls)
  {
    cout << i << " ";
  }
  cout << endl;
}

void print(const vector<string>& ls)
{
  for(auto i : ls)
  {
    cout << i << " ";
  }
  cout << endl;
}

void test50()
{
  istream_iterator<int> int_it(cin), int_eof;

  vector<int> v;
  copy(int_it, int_eof, back_inserter(v));
  sort(v.begin(), v.end());
  
  ostream_iterator<int> out_iter(cout, " ");
  cout << endl;
  unique_copy(v.begin(), v.end(), out_iter);
  
}

string &trans(string &s)
{
  for (int p = 0; p < s.size(); p++)
  {
    if (s[p] >= 'A' && s[p] <= 'Z')
    {
      s[p] -= ('A' - 'a');
    }
    else if(s[p] == ',' || s[p] == '.')
      s.erase(p, 1);
  }
  return s;
}

void test51()
{
  map<string, int> word_cout;
  string tmp;
  while(cin >> tmp)
  {
    word_cout[trans(tmp)] += 1;
  }
  for(const auto& elem:word_cout)
  {
    cout << elem.first << ":" << elem.second << endl;
  }

}

void add_family(map<string, vector<string>> &families, const string &family)
{
    families[family];
}

void add_child(map<string, vector<string>> &families, const string &family, const string &child)
{
  families[family].push_back(child);
}


int main(int argc, char **argv)
{  
  ifstream in(argv[1]);  //打开文件
  vector<pair<string, int>> data;
  string s;
  int v;

  while(in >> s && in >> v)
  {
    data.push_back(pair<string, int>(s, v));
  }

  for(const auto &d : data)
    cout << d.first << " " << d.second << endl;
}

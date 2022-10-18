// #include <iostream>
// #include <string>
// #include <unordered_map>
// using namespace std;

// string minWindow(string s, string t) {
//     unordered_map<char, int> need, window;
//     for (char c : t) need[c]++;

//     int left = 0, right = 0;
//     int valid = 0;
//     // 记录最小覆盖子串的起始索引及长度
//     int start = 0, len = INT_MAX;
//     while (right < s.size()) {
//         // c 是将移入窗口的字符
//         char c = s[right];
//         // 扩大窗口
//         right++;
//         // 进行窗口内数据的一系列更新
//         if (need.count(c)) {
//             window[c]++;
//             if (window[c] == need[c])
//                 valid++;
//         }

//         // 判断左侧窗口是否要收缩
//         while (valid == need.size()) {
//             // 在这里更新最小覆盖子串
//             if (right - left < len) {
//                 start = left;
//                 len = right - left;
//             }
//             // d 是将移出窗口的字符
//             char d = s[left];
//             // 缩小窗口
//             left++;
//             // 进行窗口内数据的一系列更新
//             if (need.count(d)) {
//                 if (window[d] == need[d])
//                     valid--;
//                 window[d]--;
//             }                    
//         }
//     }
//     // 返回最小覆盖子串
//     return len == INT_MAX ?
//         "" : s.substr(start, len);
// }
// int main(){
//     string s = "ADOBECODEBANC";
//     string t = "ABC";
//     string a;
//     a = minWindow(s, t);
//     cout << a << endl;
// }

#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int main(int argc, char **argv)
{
    int arr[] = {99, 15, 100, 888, 252};
    int i = 0, *p =arr;
    *p++;
    printf("%d", *p++);
    ++*p;
    printf("%d", ++*p);
    printf("\n");
    return 0;
}
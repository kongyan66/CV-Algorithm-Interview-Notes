# 目的：判断两个单词是否字母相同
# 方法：查询问题想哈希

def solution1(str1, str2):
    record = [0] * 26
    for i in range(len(str1)):
        # 并不需要记住字符a的ASCII，只要求出一个相对数值就可以了
        record[ord(str1[i]) - ord('a')] += 1

    for i in range(len(str2)):
        record[ord(str2[i]) - ord('a')] -= 1

    for i in range(len(record)):
        if record[i] != 0:
            return False
            break

    return True

def solution2(str1, str2):
    from collections import defaultdict
    s_dict = defaultdict(int)
    t_dict = defaultdict(int)
    for x in str2:
        s_dict[x] += 1
    for x in str1:
        t_dict[x] += 1

    return s_dict == t_dict
        
if __name__ == "__main__":
    str1 = 'adc'
    str2 = 'cda'
    print(solution2(str1, str2))
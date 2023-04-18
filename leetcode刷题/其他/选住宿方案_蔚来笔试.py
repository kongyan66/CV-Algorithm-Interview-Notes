'''
题描描述：
丽江河边有n家客栈，编号为1-n。每家客栈按照某种色调装饰，共K种，编号为0-k-1。每家都设有一家咖啡店，均设置有最低消费。
两位旅客去旅行，他们住在色调相同的两家客栈中，打算选择一家咖啡店喝咖啡，咖啡店位于两人客栈之间，且最低消费不超过p。
问有多少种住宿方案？
输入描述：
输入文件hotel.in, 共n+1行
第一行三个整数n, k, p. 空格分开，分别表示客栈个数，色调数，能接受最低消费的最高值
接下来n行，第i+1行两个数，空格隔开，分别表示i号客栈的装饰色调和咖啡店的最低消费。
输出描述：
输出只有一行，一个整数，表示可选住宿方案的总数。

'''
# 参考：https://www.shuzhiduo.com/A/nAJv0nXodr/
# 还是不会啊
def solution(n, k, p, hotels):
    for i in range(1, n):
        if hotel[i][1] <= p:
            m = i
        if m 




if __name__ == "__main__":
    # 处理
    n, k, p = map(int, input().split())
    hotels = []
    for _ in range(n):
        hotel = list(map(int, input().split()))
        hotels.append(hotel)

    


        
    
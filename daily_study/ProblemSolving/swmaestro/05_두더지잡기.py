# 두더지 잡기
from sys import*
input = stdin.readline
n = int(input())
dic = {}
for i in range(n**2):
    info = list(map(int, input().split()))
    score = info[0]
    k = info[1]
    for j in range(k):
        time = info[j+2]    #0, 1 인덱스는 제외해야하므로
        if time in dic:
            if dic[time] < score:
                dic[time] = score
        else:
            dic[time] = score
res = 0
# print(dic)
for k, v in dic.items():
    res += v
print(res)
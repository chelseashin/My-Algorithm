import sys
sys.stdin = open('8958.txt')

N = int(input())
for _ in range(N):
    quiz = input()
    cnt = 0
    temp = 0
    for i in quiz:
        if i == "X":
            temp = 0
        else:
            temp += 1
            cnt += temp
    print(cnt)
# 10
# 9
# 7
# 55
# 30
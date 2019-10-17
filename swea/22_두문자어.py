import sys
sys.stdin = open('22_input.txt')

T = int(input())
for tc in range(T):
    abc = list(map(str, input().split()))
    answer = ""
    for i in range(len(abc)):
        answer += abc[i][0].upper()
    print("#{} {}".format(tc+1, answer))
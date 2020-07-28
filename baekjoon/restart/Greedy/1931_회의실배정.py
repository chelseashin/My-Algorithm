import sys
sys.stdin = open('1931_input.txt')

N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]
time.sort(key = lambda x:(x[1], x[0]))
ans = 0
endTime = 0
for t in range(N):
    if endTime <= time[t][0]:
        endTime = time[t][1]
        ans += 1
print(ans)
import sys
sys.stdin = open("13458_input.txt")
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
ans = 0
for students in A:
    students -= B
    ans += 1
    if students < 0:
        continue
    if students % C:
        ans += students // C + 1
    else:
        ans += students // C
print(ans)
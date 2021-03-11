# 플로이드 와샬! 이라는 알고리즘이 있다고 한다.
# 처음 혼자 힘으로 금방 풀었지만, 스스로 엣지 케이스를 여러개 생각해냈고
# 이를 만족시키기 위한 알고리즘이 필요하다고 느꼈다. ==> 플로이드 와샬

# 실패 코드
import sys
input = sys.stdin.readline

N, T = map(int, input().split())
info = dict()
for n in range(1, N+1):
    info[n] = list(map(int, input().split()))
# print(info)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    # print(a, b)
    if info[a][0] and info[b][0]:
        print(min(T, abs(info[a][1] - info[b][1]) + abs(info[a][2] - info[b][2])))
    else:
        # print(a, b, info[a], info[b])
        print(abs(info[a][1] - info[b][1]) + abs(info[a][2] - info[b][2]))
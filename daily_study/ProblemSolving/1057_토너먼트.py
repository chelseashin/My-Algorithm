import sys
input = sys.stdin.readline

# 참가자 수, 지민 번호, 한수 번호
N, J, H = map(int, input().split())

# 방법 1
# cnt = 0
# while J != H:   # 두 사람이 같지 않을 동안 계속 시행
#     J -= J // 2
#     H -= H // 2
#     cnt += 1
# print(cnt)


# 방법 2
# 번호 홀수이면 + 1, 짝수이면 그대로 리턴
def idx(n):
    if n % 2:
        return n+1
    else:
        return n

cnt = 0
while True:
    cnt += 1
    J = idx(J)
    H = idx(H)
    if J == H:
        print(cnt)
        break
    # 다음 라운드로 넘어갈 때는 나누기 2한 번호가 됨
    J //= 2
    H //= 2
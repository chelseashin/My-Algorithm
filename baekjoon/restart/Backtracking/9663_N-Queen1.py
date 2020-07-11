# 성공 1

def queenlocation(depth):
    global cnt
    # 마지막 행까지 가면 카운트
    if depth == N:
        cnt += 1
        return
    for c in range(N): # 열 이동하며 검사
        # 세 조건에 걸리지 않는다면
        if row[c] + left[depth+c] + right[N-1 + depth-c] == 0:
            row[c] = left[depth+c] = right[N-1+depth-c] = 1
            queenlocation(depth+1)
            row[c] = left[depth+c] = right[N-1+depth-c] = 0

N = 8
# N = int(input())
cnt = 0
#인덱스의 합과 차가 같은 대각선상에 있을 때 같다는 것을 이용함
#ex)0,2과 1,1과 2,0은 같은 대각선상에 위치한다. 각 행열의 합이 같은것을 알 수 있다.
row = [0 for _ in range(N)]
left = [0 for _ in range(2*N-1)]
right = [0 for _ in range(2*N-1)]
queenlocation(0)
print(cnt)
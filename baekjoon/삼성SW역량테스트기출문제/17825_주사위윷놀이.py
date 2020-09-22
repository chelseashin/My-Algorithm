import sys
sys.stdin = open('17825_input.txt')
input = sys.stdin.readline

# 몇 번째 주사위인지, 점수
def solve(depth, score):
    global horse, visited, MAX
    res = 0
    if depth == 10:
        return score
    h = [x[:] for x in horse]
    v = [x[:] for x in visited]
    for i in range(4):
        d, x = horse[i]     # 방향, 인덱스
        prev = move[depth]
        nd = d
        nx = x + prev
        if x == MAX:
            continue
        # 방향 0이고, 확인할 인덱스가 내부에 들어갈 인덱스면
        if d == 0 and (x in [5, 10, 15]):
            nd = x // 5
            nx = prev
            # d==0, x==20 과 d==4, x==3이 칸 중복되어서 따로 처리
        if nd == 0 and nx == 20:
            nd = 4
            nx = 3
        # 1, 2, 3 크기 넘어갈 때
        if nd in [1, 2, 3] and (len(A[nd]) <= nx):
            nx -= len(A[nd])
            nd = 4
        # 도착
        if len(A[nd]) <= nx:
            horse[i] = [0, MAX]
            visited[d][x] = 0
            res = max(res, solve(depth+1, score))
        else:
            if visited[nd][nx]:
                continue
            horse[i] = [nd, nx]
            visited[nd][nx] = 1     # 새 위치로 이동
            visited[d][x] = 0
            res = max(res, solve(depth+1, score+A[nd][nx]))
        horse = [x[:] for x in h]
        visited = [x[:] for x in v]
    # print('horse', horse)
    return res

# main
move = list(map(int, input().split()))  # 이동 정보
A = [[2*i for i in range(21)]]  # A[0] : 테두리
A.append([10, 13, 16, 19])      # A[1] : 5번째 칸 갈 때 이동방향 
A.append([20, 22, 24])          # A[2] : 10번째
A.append([30, 28, 27, 26])      # A[3] : 15번째
A.append([25, 30, 35, 40])      # A[4] : 내부 마지막
# print(A)
MAX = float('-inf')
visited = [[0] * 21 for _ in range(5)]  # 1차 : 방향, 2차 : 인덱스
horse = [[0, 0] for _ in range(4)]      # 1차 : 말 번호, 2차 : [방향, 인덱스]
# for v in visited:
#     print(v)

print(solve(0, 0))
import sys
sys.stdin = open('16235_input.txt')

# 번식할 수 있는 8 방향 좌표
dr = (-1, 1, 0, 0, -1, -1, 1, 1)
dc = (0, 0, -1, 1, -1, 1, -1, 1)

# main
N, M, K = map(int, input().split())
vitamin = [list(map(int, input().split())) for _ in range(N)]

# 현재 양분의 상태
A = [[5]*N for _ in range(N)]

# 현재 땅의 상태(숫자는 나이를 표시)
tree = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

# 매년 사계절이 흐름
for year in range(K):
    # 봄, 여름
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                tree[i][j].sort()
                temp_tree, dead_tree = [], 0
                for age in tree[i][j]:
                    if age <= A[i][j]:
                        A[i][j] -= age              # 양분 먹기
                        temp_tree.append(age+1)     # 나이 먹기
                    else:
                        # 양분이 부족해 죽은 나무는 나이를 저장
                        dead_tree += age // 2
                A[i][j] += dead_tree
                tree[i][j] = temp_tree
    
    # 나무 없으면 종료
    if not tree:
        print(0)
        sys.exit()

    # 가을
    for r in range(N):
        for c in range(N):
            if tree[r][c]:
                for age in tree[r][c]:
                    if not age % 5:
                        for dir in range(8):
                            nr = r + dr[dir]
                            nc = c + dc[dir]
                            if (0 <= nr < N and 0 <= nc < N):
                                tree[nr][nc].append(1)
    # 겨울
    for i in range(N):
        for j in range(N):
            A[i][j] += vitamin[i][j]    # 양분 추가

ans = 0
for i in range(N):
    for j in range(N):
        if tree[i][j]:
            ans += len(tree[i][j])
print(ans)
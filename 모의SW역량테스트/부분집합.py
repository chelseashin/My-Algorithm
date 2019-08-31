arr = 'ABC'
N = len(arr)
order = [0] * N

# 순열 함수
def perm(k, n, visited):     # visited : 지금까지 선택한 요소들의 집합
    if k == n:
        pass
    else:
        # 아직 선택되지 않은 요소들을 찾는다.
        for i in range(n):
            if visited & (1 << i): continue
            order[k] = i
            perm(k+1, n, visited | (1 << i))

print(perm(0, N, 0))

for i in range(N):
    for j in range(N):
        if i == j: continue
        for k in range(N):
            if k == i or k == j:
                continue
            print(arr[i], arr[j], arr[k])

n = 10

for i in range(4):
    if n & (1 << i): print(1, end=" ")
    else: print(0, end=' ')
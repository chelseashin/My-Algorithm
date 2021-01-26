# 해시를 활용한 Union-Find 알고리즘을 이용

import sys
input = sys.stdin.readline

# 재귀로 자신의 부모를 찾는 함수
def find_parent(x):
    if x == parent[x]:
        return x
    else:
        root_x = find_parent(parent[x])
        parent[x] = root_x
        return parent[x]

# y의 Root 노드가 x의 Root 노드와 같지 않으면
# y의 Root 노드가 x의 Root 노드의 자식이 되도록 하는 함수
def union(x, y):
    root_x = find_parent(x)
    root_y = find_parent(y)

    if root_x != root_y:
        parent[root_y] = root_x
        number[root_x] += number[root_y]

T = int(input())
for _ in range(T):
    F = int(input())
    parent = dict()
    number = dict()
    for _ in range(F):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        union(a, b)     # a와 b 연결하기
        
        print(number[find_parent(a)])
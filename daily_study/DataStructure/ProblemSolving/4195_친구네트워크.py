# 해시를 활용한 Union-Find 알고리즘을 이용

import sys
input = sys.stdin.readline

# 재귀로 자신의 부모를 찾는 함수
def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

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
        # print("parent", parent)
        # print("number", number)
        union(a, b)     # a와 b 연결하기
        
        print(number[find(a)])
# Union-Find 알고리즘 - 합집합 찾기
# 원소들의 연결여부를 확인

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
    parent[y] = x

parent = []
for i in range(5):
    parent.append(i)
print(parent)
union(1, 4)
union(2, 4)

print(parent)
for i in range(1, len(parent)):
    print(find(i), end=" ")
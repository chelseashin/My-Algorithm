# def main():
#     skills = list(input().split())
#     n = int(input())
#     for _ in range(n):
#         x, y = input().split()
#         print(x, y)
#     print(skills, n)
#
# if __name__ == "__main__":
#     main()


# 소마 스토리 앤 파이터
from sys import*
input = lambda:stdin.readline().strip()
def dfs(u, str):
    str += u + " "
    if u not in adj:
        print(str)
        return
    for v in adj[u]:
        dfs(v, str)
skills = list(map(str, input().split()))
adj = {}
rootException = set()
for i in range(int(input())):
    u, v = map(str,input().split())
    # 이런 입력이 올지는 모르겠는데 암튼 단독스킬 단독 사용 없다는 조건 처리
    if u == v:
        continue
    rootException.add(v)
    if u not in adj:
        adj[u] = [v]
    else:
        adj[u].append(v)
print("adj", adj)
print("rootException", rootException)
for k, v in adj.items():
    if k not in rootException:
        dfs(k, "")

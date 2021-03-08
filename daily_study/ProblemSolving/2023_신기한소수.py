def solve(depth, temp):
    # 소수 가지치기
    for p in range(2, int(int(temp)**0.5)+1):
        if not int(temp) % p:
            return

    if depth == n:
        print(temp)
        return

    for i in "1379":
        solve(depth+1, temp+i)

n = int(input())
for s in "2357":
    solve(1, s)
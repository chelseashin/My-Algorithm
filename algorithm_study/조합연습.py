def solve(s: list):
    if len(s) == 3:
        print(*s)
        return
    start = 0
    if s:
        start = s[-1]
    for i in range(start, len(arr)):
        if arr[i] not in visit:
            visit.add(arr[i])
            s.append(arr[i])
            solve(s)
            s.pop()
            visit.remove(arr[i])


# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
arr = list(range(1, 13))
arr.sort()
visit = set()
solve([])
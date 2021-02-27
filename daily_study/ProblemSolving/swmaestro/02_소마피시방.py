def solve(pos, i, total, h):
    global arr
    res = 0
    if pos == len(arr[i]):
        return total
    if total + arr[i][pos] <= h:
        res = max(res, solve(pos+1, i, total + arr[i][pos], h))
    res = max(res, solve(pos+1, i, total, h))
    return res

def main():
    global arr
    price = 1000
    p, n, h = map(int, input().split())
    arr = [[] for _ in range(p + 1)]
    for i in range(n):
        pcNum, usingTime = map(int, input().split())
        if usingTime > h:
            continue
        arr[pcNum].append(usingTime)
    for i in range(1, p + 1):
        print(i, solve(0, i, 0, h) * price)

if __name__ == "__main__":
    main()


# 소마 피시방
# from sys import*
# input = stdin.readline
# def solve(pos, i, total):
#     res = 0
#     if pos == len(arr[i]):
#         return total
#     if total + arr[i][pos] <= h:
#         res = max(res, solve(pos+1, i, total + arr[i][pos]))
#     res = max(res, solve(pos+1, i, total))
#     return res
#
# PRICE = 1000
# p, n, h = map(int ,input().split())
# arr = [[]for i in range(p+1)]
# for i in range(n):
#     pcNum, usingTime = map(int,input().split())
#     if usingTime > h: continue
#     arr[pcNum].append(usingTime)
# for i in range(1, p+1):
#     print(i, solve(0, i, 0) * PRICE)
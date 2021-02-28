# def solve(pos, i, total, h):
#     global arr
#     res = 0
#     if pos == len(arr[i]):
#         return total
#     if total + arr[i][pos] <= h:
#         res = max(res, solve(pos+1, i, total + arr[i][pos], h))
#     res = max(res, solve(pos+1, i, total, h))
#     return res
#
# def main():
#     global arr
#     price = 1000
#     p, n, h = map(int, input().split())
#     arr = [[] for _ in range(p + 1)]
#     for i in range(n):
#         pcNum, usingTime = map(int, input().split())
#         if usingTime > h:
#             continue
#         arr[pcNum].append(usingTime)
#     for i in range(1, p + 1):
#         print(i, solve(0, i, 0, h) * price)
#
# if __name__ == "__main__":
#     main()


def solve(idx, time, pay, h, info):
    global temp
    if time >= h:
        temp = max(temp, pay)
        return
    for t in info[idx]:
        if time + t <= h:
            solve(idx, time+t, pay + 1000 * t, h, info)

def main():
    global temp
    p, n, h = map(int, input().split())
    info = {}
    for _ in range(n):
        x, y = map(int, input().split())
        if y > h:
            continue
        if x not in info.keys():
            info[x] = [y]
        else:
            info[x].append(y)
    for i in range(1, p+1):
        if i not in info.keys():
            print(i, 0)
        else:
            temp = 0
            solve(i, 0, 0, h, info)
            print(i, temp)

if __name__ == "__main__":
    main()
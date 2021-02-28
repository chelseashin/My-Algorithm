def main():
    n, m, e = map(int, input().split())
    pos = list(map(int, input().split()))
    info = dict()
    for p in pos:
        if abs(e-p) in info.keys():
            info[abs(e-p)].append(p)
        else:
            info[abs(e-p)] = [p]
    MIN = float('inf')
    MAX = float('-inf')
    i = 0
    while m:
        if i not in info.keys():
            i += 1
            continue
        for dis in info[i]:
            if m:
                m -= 1
                MIN = min(MIN, dis)
                MAX = max(MAX, dis)
            if not m:
                break
        i += 1
    print(MAX - MIN)

if __name__ == "__main__":
    main()
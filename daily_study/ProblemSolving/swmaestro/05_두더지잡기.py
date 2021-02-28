# 두더지 잡기
def main():
    n = int(input())
    info = {}
    for _ in range(n*n):
        temp = list(map(int, input().split()))
        score = temp[0]
        for i in range(temp[1]):
            time = temp[i+2]     # 0, 1 인덱스는 제외해야하므로
            if time not in info.keys():
                info[time] = score
            else:
                info[time] = max(info[time], score)
    answer = 0
    for s in info.values():
        answer += s
    print(answer)

if __name__ == "__main__":
    main()
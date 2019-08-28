import sys
sys.stdin = open("01_input.txt")

def bfs():
    global cards, asc, desc, N, n
    Q = []
    while Q:
        s = Q.pop(0)
        # 가지치기(도착하면)
        if cards == asc or cards == desc:
            return
        else:
            # n이 N//2보다 작다면
            if n < N//2:
                for i in range(N//2):
                    Card.append(card_L[i])
                    Card.append(card_R[-i])
            # n이 N//2보다 크거나 같다면
            else:


T = int(input())
for tc in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    asc = sorted(cards)                 # 오름차순
    desc = sorted(cards, reverse=True)  # 내림차순
    count = 0

    # 원래 오름차순, 내림차순 정렬일 때
    if cards == asc and cards == desc:
        count = 0
    else:
        Card = []
        card_L = cards[:N // 2]
        card_R = cards[N // 2:]
        for n in range(1, N):
            # 카드 i번 만큼 셔플
            bfs()
            count += 1

    print("#{} {}".format(tc+1, count))
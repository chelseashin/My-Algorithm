import sys
sys.stdin = open("01_input.txt")

def dfs(depth, x, card):
    global cards, asc, desc, N, result
    # 가지치기 : depth는 5회까지. result보다 크면 cut
    if depth == 6 or depth >= result:
        return
    if card == asc or card == desc:
        result = min(result, depth)
        return
    card_L = card[:N//2]
    card_R = card[N//2:]
    if x >= N//2:
        temp = card_R[:(x+1) - N//2]
        card_R = card_R[(x+1) - N//2:]
    else:
        temp = card_L[:N//2-(x+1)]
        card_L = card_L[N//2-(x+1):]
    while (card_L or card_R):
        if card_L:
            temp.append(card_L.pop(0))
        if card_R:
            temp.append(card_R.pop(0))
    for i in range(1, N):
        if x == 1 and i == 1:
            continue
        dfs(depth+1, i, temp)

T = int(input())
for tc in range(T):
    N = int(input())    # 카드 개수
    cards = list(map(int, input().split()))
    asc = sorted(cards)                 # 오름차순
    desc = sorted(cards, reverse=True)  # 내림차순
    result = float('inf')               # 셔플 횟수의 최소값

    for i in range(1, N):
        # dfs(depth, x(셔플방법), 현재카드상태)
        dfs(0, i, cards)
    if result == float('inf'):
        result = -1

    print("#{} {}".format(tc+1, result))
import sys
sys.stdin = open("18_input.txt")

def card_split(start, end):
    # 카드 하나인 경우
    if (end - start) == 0:
        return start
    elif (end - start) == 1:
        if cards[start] - cards[end] == 1 or cards[start] - cards[end] == -2 or cards[start] - cards[end] == 0:
            return start
        else:
            return end

    a = card_split(start, (start+end)//2)
    b = card_split((start+end)//2+1, end)
    if cards[a]-cards[b] == 1 or cards[a]-cards[b] == -2 or cards[a]-cards[b] == 0:
        return a
    else:
        return b

T = int(input())
for tc in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    # print(cards)
    pos = card_split(0, N-1)    # 번호 시작과 끝
    print("#{} {}".format(tc+1, pos+1))
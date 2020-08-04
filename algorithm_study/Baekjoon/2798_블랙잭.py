import sys
sys.stdin = open('2798_input.txt')

# 인덱스, 몇 개 선택했는지, 합계
def solve(pos, cnt, temp):
    ans = float('inf')
    if temp > M or cnt > 3:
        return ans
    if pos == N:
        if cnt == 3:
            return abs(temp - M)
        return ans
    ans = min(ans, solve(pos+1, cnt+1, temp+cards[pos]))
    ans = min(ans, solve(pos+1, cnt, temp))
    return ans

N, M = map(int, input().split())
cards = list(map(int, input().split()))
print(cards)

# 카드 3장의 합은 M보다 작거나 같음
print(M-solve(0, 0, 0))
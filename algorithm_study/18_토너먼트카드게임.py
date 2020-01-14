import sys
sys.stdin = open("18_input.txt")

def card_split(start, end):


T = int(input())
for tc in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    print("#{} {}".format(tc+1, card_split(0, N-1)+1))
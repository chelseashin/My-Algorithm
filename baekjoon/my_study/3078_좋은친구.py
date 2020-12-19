import sys
sys.stdin = open("3078_input.txt")
input = sys.stdin.readline

# 시간초과..
def comb(depth, k):
    global pair
    if depth == 2:
        print(order)
        if friends[order[0]] == friends[order[1]]:
            pair += 1
        return
    for i in range(K):

        order.append(k+i)
        comb(depth+1, i+1)
        order.pop()

N, K = map(int, input().split())
friends = [len(input().strip()) for _ in range(N)]
# print(friends)

pair = 0
order = []
comb(0, 0)
print(pair)

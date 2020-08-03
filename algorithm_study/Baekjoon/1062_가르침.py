import sys
sys.stdin = open('1062_input.txt')

D = dict()
raw = {'a', 'c', 'i', 't', 'n'}
raw = len(D)
print(raw, D)

N, K = map(int, input().split())
cnt = 0
for _ in range(N):
    word = input()[4:-4]
    # print(word[4:-4])
    print(word)
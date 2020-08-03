import sys
sys.stdin = open('1339_input.txt')

# python 내장함수 pow
# pow(a, b) : a의 b제곱을 계산해서 반환해주는 내장함수
# print(pow(10, 6))
# 결과로 1000000

# Greedy로 풀어보았음!
N = int(input())
words = []
for _ in range(N):
    words.append(list(input()))
# print(words)
# 알파벳에 대해 자리를 세서 중요도를 기록하는 리스트
alphabet = [0] * 26

for word in words:
    i = 0
    while word:
        alphabet[ord(word[-1]) - ord('A')] += 10 ** i
        # print(alphabet)
        i += 1
        word.pop()
# 내림차순 sort
# print(alphabet)
alphabet.sort(reverse=True)
# print(alphabet)
# 높은 순으로 9부터 1까지 곱해줌
ans = 0
for i in range(9, 0, -1):
    ans += i * alphabet[9-i]
print(ans)
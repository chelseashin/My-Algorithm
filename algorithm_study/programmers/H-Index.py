import sys
sys.stdin = open("input.txt")

citations = sorted(list(map(int, input().split())))

# 방법 1
# citations.sort()
# N = len(citations)
# answer = 0
# for i in range(N):
#     if citations[i] >= N - i:
#         answer = N - i
#         break
# print(answer)


# citations.sort(reverse=True)
# answer = max(map(min, enumerate(citations, start=1)))
# print(answer)


# 방법 2
citations.sort(reverse=True)
for i in range(len(citations)):
    if citations[i] <= i:
        answer = i
        break
print(answer)
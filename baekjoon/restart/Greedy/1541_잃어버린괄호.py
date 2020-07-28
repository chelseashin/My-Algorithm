import sys
sys.stdin = open('1541_input.txt')

expression = input().split('-')
# print(expression)

partial_sum = []
for t in expression:
    temp = list(map(int, t.split('+')))
    partial_sum.append(sum(temp))

total = partial_sum[0]
for psum in partial_sum[1:]:
    total -= psum

print(total)
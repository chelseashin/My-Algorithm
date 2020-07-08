N = 26
# N = int(input())
# 1
# temp = N
# cnt = 0
# while True:
#     a = N // 10
#     b = N % 10
#     one = a + b
#     N = int(str(N%10) + str(one%10))
#     cnt += 1
#     if N == temp:
#         break
# print(cnt)

raw = N
cnt = 0
while True:
    temp = N//10 + N%10
    new = (N%10) * 10 + temp%10
    N = new
    cnt += 1
    if new == raw:
        break
print(cnt)
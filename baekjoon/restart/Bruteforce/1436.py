N = 2
# N = int(input())
six = 666

# 방법 1
cnt = 0
while True:
    if '666'in str(six):
        cnt += 1
    if cnt == N:
        print(six)
        break
    six += 1

# 방법 2
# while N:
#     if '666' in str(six):
#         N -= 1
#     six += 1
# print(six-1)

# 1. 666
# 2. 1666
# 3. 2666
# 4. 3666
# 5. 4666
# 6. 5666
# 7. 6660
# 8. 6661 ...
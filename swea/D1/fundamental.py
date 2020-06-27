import sys
sys.stdin = open("input.txt")

# 2072. 홀수만 더하기
# T = int(input())
# for tc in range(T):
#     L = list(map(int, input().split()))
#     ans = 0
#     for i in L:
#         if i % 2 == 1:
#             ans += i
#     print("#{} {}".format(tc+1, ans))

# 2071. 평균값 구하기
# T = int(input())
# for tc in range(T):
#     L = list(map(int, input().split()))
#     s = 0
#     for i in L:
#         s += i
#     print("#{} {}".format(tc+1, round(s / len(L))))

# 2070. 큰놈 작은놈 같은놈
# T = int(input())
# for tc in range(T):
#     a, b = map(int, input().split())
#     if a < b:
#         ans = "<"
#     elif a > b:
#         ans = ">"
#     else:
#         ans = "="
#     print("#{} {}".format(tc + 1, ans))

# 2068. 큰 수 구하기
# T = int(input())
# for tc in range(T):
#     ans = float('-inf')
#     L = list(map(int, input().split()))
#     for i in L:
#         if i > ans:
#             ans = i
#     print("#{} {}".format(tc + 1, ans))

# 2063. 중간값 구하기
# n = int(input())
# L = sorted(list(map(int, input().split())))
# ans = L[n//2]
# print(ans)

# 2058. 자릿수 더하기
# n = str(input())
# ans = 0
# for i in n:
#     ans += int(i)
# print(ans)

#2056. 연월일달력

# T = int(input())
# for tc in range(T):
#
#     YMD = input()
#     ans = YMD[:4] + "/"
#     if 1 <= int(YMD[4:6]) <= 12:
#         ans += YMD[4:6] + "/"
#         if YMD[4:6] == "02":
#             if 1 <= int(YMD[6:]) <= 28:
#                 ans += YMD[6:]
#             else:
#                 ans = "-1"
#         else:
#             if YMD[4:6] in ["01", "03", "05", "07", "08", "10", "12"]:
#                 if 1 <= int(YMD[6:]) <= 31:
#                     ans += YMD[6:]
#                 else:
#                     ans = "-1"
#             else:
#                 if 1 <= int(YMD[6:]) <= 30:
#                     ans += YMD[6:]
#                 else:
#                     ans = "-1"
#     else:
#         ans = "-1"
#
#     print("#{} {}".format(tc + 1, ans))

# T = int(input())
# for tc in range(1,T+1):
#     N = input()
#     Y=N[0:4]
#     M=N[4:6]
#     D=N[6:8]
#     a=[31,28,31,30,31,30,31,31,30,31,30,31]
#     if 1 <= int(M) <= 12 and int(D) <= a[int(M)-1] and int(D) != 0:
#         print('#{} {}/{}/{}'.format(tc,Y,M,D))
#     else:
#         print('#{} -1'.format(tc))

# 2050. 알파벳을 숫자로 변환
# S = input()
# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# for i in S:
#     I = alphabet.index(i)
#     print(I+1, end=" ")

# s = input()
# for i in range(len(s)):
#     x = ord(s[i]) - 65 + 1
#     print(x, end=" ")

# 2047. 신문 헤드라인
# print(input().upper())

# 2046. 스탬프 찍기
# print("#" * int(input()))

# 2043. 서랍의 비밀번호
# a, b = map(int, input().split())
# if a > b:
#     ans = a-b+1
# else:
#     a, b = b, a
#     ans = a - b + 1
# print(ans)

# 2029. 몫과 나머지 출력하기
# T = int(input())
# for tc in range(1,T+1):
#     a, b = map(int, input().split())
#
#     print("#{} {} {}".format(tc, a//b, a%b))


# 2027. 대각선 출력하기
# for i in range(5):
#     for j in range(5):
#         if i == j:
#             print("#", end="")
#         else:
#             print("+", end="")
#     print()

# 2025. N줄덧셈
# N = int(input())
# ans = 0
# for i in range(1, N+1):
#     ans += i
# print(ans)

# 1938. 아주 간단한 계산기
# a, b = map(int, input().split())
# print(a+b)
# print(abs(a-b))
# print(a*b)
# print(a//b)

# 1933. 간단한 N 의 약수
# N = int(input())
# for i in range(1, N+1):
#     if N%i == 0:
#         print(i, end=" ")

# 1936. 1대1 가위바위보
# a, b = map(int, input().split())
# if a > b: print("A")
# else: print("B")

# 2019. 더블더블
# N = int(input())
# for i in range(N+1):
#     print(2 ** i, end=" ")

# 1545. 거꾸로 출력해 보아요
# N = int(input())
# for i in range(N, -1, -1):
#     print(i, end =" ")
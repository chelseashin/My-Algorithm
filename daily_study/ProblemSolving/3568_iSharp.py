# 알고리즘 분류 : 문자열 처리
# int&과 같이 공통된 타입을 분리한다.
# 각 변수마다 공통된 타입 + 역순으로 자신의 타입을 출력한다.
# []의 경우 역순으로 출력하지 않도록 주의.
# 처음 알파벳이 나온 경우, 한칸 띄우고 출력하여야 한다.
# 알파벳 역시 변수명이므로 역순으로 출력하지 않도록 주의.

# 나의 코드 - 성공!
import sys
input = sys.stdin.readline

variables = list(input().split())
vlen = len(variables)
for i in range(1, vlen):
    temp = variables[0]
    idx = len(variables[i])-1
    while True:
        if variables[i][idx] == ";" or variables[i][idx] == ",":
            idx -= 1
        elif variables[i][idx] == "]":
            temp += "[]"
            idx -= 2
        elif variables[i][idx] == "*":
            temp += "*"
            idx -= 1
        elif variables[i][idx] == "&":
            temp += "&"
            idx -= 1
        else:           # 띄어쓰기 만나면 종료
            break
    print(temp + " " + variables[i][:idx+1] + ";")

# 다른 성공 풀이..
# from sys import stdin, stdout
# input = stdin.readline
# print = stdout.write
#
# def solve(s):
#     for i in range(len(s)-2, -1, -1):
#         if s[i] == ']':
#             print('[]')
#         elif s[i] == '[':
#             continue
#         elif s[i] in '&*':
#             print(s[i])
#         else:
#             print(' ')
#             for j in range(0, i+1):
#                 print(s[j])
#             print(';\n')
#             return
#
# datatype, *variable = input().split()
# for s in variable:
#     print(datatype)
#     solve(s)
import sys
sys.stdin = open('16637_input.txt')
from collections import deque

def cal(n1, op, n2):
    if op == '+': return n1 + n2
    if op == '-': return n1 - n2
    if op == '*': return n1 * n2
#
def calculate():
    global S
    Q = deque()
    i = 0
    while True:
        if i == N:
            break
        if i%2 and check[i]:
            Q.append(cal(int(Q.pop()), S[i], int(S[i+1])))
            i += 1
        else:
            Q.append(S[i])
        i += 1
    while Q:
        if len(Q) == 1:
            break
        Q.appendleft(cal(int(Q.popleft()), Q.popleft(), int(Q.popleft())))
    return Q[0]

def dfs(pos):
    global MAX
    if pos >= N:
        # print(check)
        temp = calculate()
        # print(temp)
        if temp > MAX:
            MAX = temp
        return
    check[pos] = 1
    dfs(pos+4)
    check[pos] = 0
    dfs(pos+2)

N = int(input())
S = input()
MAX = -2**31
check = [0] * N

dfs(1)
print(MAX)
# print(MAX)

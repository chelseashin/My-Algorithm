import sys
sys.stdin = open('21_input.txt')

T = int(input())
for tc in range(T):
    N = str(input())
    # L = []
    # for i in range(len(N)):
    #     if N[i] not in L:
    #         L.append(N[i])
    #     else:
    #         continue
    # print("#{} {}".format(tc+1, len(L)))
    
    # 한 줄로 풀기
    print("#{} {}".format(tc+1, len(set(N))))
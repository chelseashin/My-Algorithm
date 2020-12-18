import sys
sys.stdin = open('5430_input.txt')

T = int(input())
for _ in range(T):
    p = list(input())
    n = int(input())
    L = eval(input())
    print(L)

    error = False
    R_count = 0     # 홀짝 뒤집힌 횟수
    D_front = 0     # 앞에서 없어지는 횟수

    for func in p:
        if func == "R":
            R_count += 1
        else:
            try:
                # 뒤집는 횟수가 짝수면
                if R_count % 2 == 0:
                    D_front += 1    # 나중에 빼줄 때 사용
                else:
                    L.pop()         # 지금 바로 빼주기
            except:
                error = True
                break
    # 에러 상황 거르기
    if error or D_front > len(L):
        print("error")
        continue
    
import sys
sys.stdin = open('14501_input.txt')


# 현재 날짜 d(day) 와 현재 소득 money를 인자로 가지는 함수 solve 선언
def solve(d: int, money: int):
    global maxnow  # 전역 변수 maxnow에 현재까지 도달한 최대 이익 저장
    if d >= N:  # 종료조건. 현재 날짜가 퇴사일에 도달
        if money > maxnow:  # 최대값이 갱신될경우 새로운 최대값을 저장하고 리턴
            maxnow = money
        return
    if d + arr[d][0] <= N:  # 가지치기, 현재 날짜의 상담이 실현 가능한 경우만
        solve(d + arr[d][0], money + arr[d][1])  # 상담 실행
    solve(d + 1, money)  # 상담하지 않고 내일로 진행


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 입력
maxnow = -1
# 최대값 초기화
solve(0, 0)
print(maxnow)
def solution(brown, red):
    N = brown + red
    for n in range(1, N+1):
        if N%n != 0:
            continue
        m = N//n
        if (n-2)*(m-2) == red:
            return sorted([n, m], reverse = True)

# def solution(brown, red):
#     for i in range(1, int(red**(1/2))+1):
#         if red % i == 0:
#             if 2*(i + red//i) == brown-4:
#                 return [red//i+2, i+2]

brown = 10
red = 2
print(solution(brown, red))
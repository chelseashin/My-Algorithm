board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    S = []
    N = len(board)
    for num in moves:
        for n in range(N):
            if board[n][num - 1]:
                temp = board[n][num - 1]
                board[n][num - 1] = 0
                if len(S) == 0:
                    S.append(temp)
                    break
                else:
                    if S[-1] == temp:
                        S.pop(-1)
                        answer += 2
                        break
                    else:
                        S.append(temp)
                        break
            else:
                continue
    return answer

print(solution(board, moves))
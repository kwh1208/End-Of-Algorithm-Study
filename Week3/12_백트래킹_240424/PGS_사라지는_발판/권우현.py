# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms
board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]

Min = 1000000

from collections import deque

def solution(board):
    result = 10000
    N = len(board)
    direction = [[0, 1, 0], [1, 0, 1], [0, -1, 2], [-1, 0, 3]]
    dp = [[[10000] * N for i in range(N)] for j in range(4)]
    queue = deque()
    queue.append([0, 0, 0, 0])
    queue.append([0, 0, 0, 1])
    while queue:
        x, y, m, d = queue.popleft()
        for i in range(4):
            new_x = x + direction[i][0]
            new_y = y + direction[i][1]
            if -1 < new_x < N and -1 < new_y < N and board[new_x][new_y] == 0:
                new_m = m + 1
                if not d == direction[i][2]:
                    new_m += 5
                if new_m < dp[direction[i][2]][new_x][new_y]:
                    dp[direction[i][2]][new_x][new_y] = new_m
                    if new_x == N-1 and new_y == N-1:
                        continue
                    queue.append([new_x, new_y, new_m, direction[i][2]])
    for i in range(4):
        result = min([result, dp[i][N-1][N-1]])
    return result * 100

print(solution(board))
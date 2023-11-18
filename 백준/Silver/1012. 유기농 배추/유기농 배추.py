import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                dfs(nx, ny)


    

T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(T):
    M, N, K = map(int, input().split())     # 배추 밭 가로 길이, 세로 길이, 심어져있는 배추 개수
    graph = [[0] * M for _ in range(N)]
    cnt = 0

    for i in range(K):
        x, y = map(int, input().split())    # 배추 위치 저장
        graph[y][x] = 1
    
    for x in range(M):
        for y in range(N):
            if graph[y][x] == 1:
                dfs(x, y)
                cnt += 1

    print(cnt)
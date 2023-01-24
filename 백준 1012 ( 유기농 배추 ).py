import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:     # 밭의 위치를 넘어가지 않는 경우
            if graph[ny][nx] == 1:          # 배추가 심어져있으면
                graph[ny][nx] = 0           # 값을 0으로 바꾸어 나중에 해당 위치에서 dfs가 돌아가지 않게 한다.
                dfs(nx, ny)                 # 그리고 해당 위치로 이동하여 dfs를 돌린다.

T = int(input())                            # 테스트 케이스의 개수 입력

dx = [0, 0, -1, 1]                          # 상하좌우 확인을 위한 리스트 선언
dy = [-1, 1, 0, 0]

for _ in range(T):
    M, N, K = map(int, input().split())     # M, N, K : 배추 밭 가로 길이, 세로 길이, 심어져있는 배추 개수
    graph = [[0] * M for _ in range(N)]     # 배추의 위치를 저장할 리스트
    cnt = 0                                 

    for i in range(K):
        x, y = map(int, input().split())    # 배추 위치 저장
        graph[y][x] = 1
    
    for x in range(M):                      
        for y in range(N):
            if graph[y][x] == 1:            # 배추가 심어져있으면
                dfs(x, y)                   # dfs를 돌려서 인접한 배추들을 확인한다.
                cnt += 1                    # 배추들의 그룹을 확인 하였으면 그룹의 개수를 추가한다.

    print(cnt)

# 인접한 배추들의 그룹 당 지렁이 1마리 필요함
# 그럼 dfs를 돌리는 횟수로 배추 그룹의 수를 파악하면 됨
# 그래서 배추의 위치를 저장한 위치를 돌면서 배추가 심어져있는 위치에서 dfs를 돌린다.
# 이때 dfs에서 해당 위치의 상하좌우를 확인하는데 만약 인접한 위치에 배추가 있으면 (값이 1이면)
# 그 위치의 값을 0으로 바꾸고, 그 위치로 이동하여 인접한 배추가 있는지 확인한다.
# 요약하자면 그래프를 돌면서 배추가 심어져있는 위치에서 dfs를 돌려서 그 배추와 인접한 배추들을 다 값이 1이 아닌 다른 값으로 바꾼다.
# 이렇게 하여 다음 dfs를 돌릴때 해당 위치가 걸리지 않게 하여 그룹의 개수를 파악할 수 있게한다.

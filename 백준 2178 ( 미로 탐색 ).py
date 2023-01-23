from collections import deque

N, M = map(int, input().split())

visited = [[False] * M for _ in range(N)]                            # 방문 노드 확인 리스트
distanceList = [[0] * M for _ in range(N)]                           # 거리 기록 리스트
graph = [list(map(int, input().strip())) for _ in range(N)]          # 미로 

queue = deque()                                                      # 현재 위치 저장할 큐 
queue.append((0, 0))
distanceList[0][0] = 1                                               # 시작점에서의 거리는 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 상하좌우로 이동할 수 있는 위치를 확인한다.
# dx[0] dy[0] (0, -1) : 왼쪽
# dx[1] dy[1] (0, 1) : 오른쪽
# dx[2] dy[2] (-1, 0) : 위쪽
# dx[3] dy[3] (1, 0) : 아래쪽

while queue:
    x, y = queue.popleft()                                                # 현재 위치를 x, y에 저장
    for i in range(4):
        mx, my = x + dx[i], y + dy[i]                                     # for문을 통해서 현재 위치에서 상하좌우 방향으로 이동
        if 0 <= mx < N and 0 <= my < M:                                   # 미로를 벗어나지 않는 경우
            if visited[mx][my] == False and graph[mx][my] == 1:           # 방문하지 않았고, 값이 1인 지점(이동할 수 있는 노드)이면
                queue.append((mx, my))                                    # 큐에 추가(해당 지점으로 이동)
                distanceList[mx][my] += distanceList[x][y] + 1            # 거리를 1 추가
                visited[mx][my] = True                                    # 방문 처리
                
print(distanceList[N - 1][M - 1])

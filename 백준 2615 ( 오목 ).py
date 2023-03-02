def bfs(x, y):
    if graph[x][y] != 0:
        target = graph[x][y]            

        for n in range(4):
            cnt = 1
            nx = x + dx[n]
            ny = y + dy[n]

            while 0 <= nx < 19 and 0 <= ny < 19 and graph[nx][ny] == target:        # 이동할 좌표가 범위를 벗어나지 않고, 이전 바둑알과 같은 색이라면?
                cnt += 1                                                            
                if cnt == 5:                                                        # 오목이 된 경우
                    if 0 <= x - dx[n] < 19 and 0 <= y - dy[n] < 19 and graph[x - dx[n]][y - dy[n]] == target:       # 육목인지 확인 (시작 좌표 이전에 같은 색의 바둑알이 있나?)
                        break
                    if 0 <= nx + dx[n] < 19 and 0 <= ny + dy[n] < 19 and graph[nx + dx[n]][ny + dy[n]] == target:   # 육목인지 확인 (끝 좌표 이후에 같은 색의 바둑알이 있나?)
                        break

                    print(target)                                             
                    print(x + 1, y + 1)
                    exit(0)

                nx += dx[n]                                                         # 이전에 이동했던 방향으로 이동
                ny += dy[n]                                                         # 이전에 이동했던 방향으로 이동

graph = [list(map(int, input().split())) for _ in range(19)]
# →, ↓, ↗, ↘     
dx = [0, 1, -1, 1]
dy = [1, 0, 1, 1]

for i in range(19):
    for j in range(19):
        bfs(i, j)
print(0)       

# 바둑판에 흑백 돌들이 놓여있고 이를 보고 오목 경기의 승패를 확인하는 문제이다.
# 한 색의 바둑돌이 같은 방향으로 연속 5개가 이어지면 오목이 된다. 
# 그래서 오목판에 돌이 있으면 그 돌을 타켓으로 삼고 탐색을 시작한다.
# 탐색의 방향은 총 4 방향으로 우, 하, 우상, 우하 방향으로 탐색을 진행한다. (문제에서 오목이 시작되는 가장 왼쪽에 있는 바둑알(연속된 다섯 개의 바둑알이 세로로 놓인 경우, 그 중 가장 위에 있는 것)을 출력하라고 했기 때문)
# 판의 범위를 벗어나지 않고, 이동한 방향에 있는 돌이 타켓과 같다면 카운트를 증가한다.
# 만약 카운트가 5가 되면 오목이 된 것인데 문제에서 육목은 무효라고 했기 때문에 육목인지 확인을 하고 아니면 타켓을 출력하고, 오목이 시작되는 좌표를 출력한다.
# 만약 승패가 갈리지 않은 경우에는 0을 출력한다.    

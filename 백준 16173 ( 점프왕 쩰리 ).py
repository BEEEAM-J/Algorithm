import sys
sys.setrecursionlimit(10000)

def bfs(x, y):
    global ans
    
    dx = []
    dy = []

    # 위치 이동을 위한 리스트 생성 (아래, 오른쪽 순서)
    dx.append(graph[x][y])
    dx.append(0)
    
    dy.append(0)
    dy.append(graph[x][y])
        
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:     # 범위를 벗어나지 않는다면
            if graph[nx][ny] == -1:         # 만약 도착지에 도착한다면 "HaruHaru"를 출력하고 종료를 한다.
                print("HaruHaru")
                exit()
            if graph[nx][ny] == 0:          # 만약 값이 0이면 이동이 아예 불가하므로 뒤로 돌아간다.
                break
            bfs(nx, ny)
        
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)] 
ans = 0
bfs(0, 0)
print("Hing")                               # 도착지에 도착하지 못했을 경우에 나오게 되므로 "Hing"을 출력한다.

# 젤리는 아래, 오른쪽 방향으로만 이동이 가능하다. 
# 그래서 dx, dy 리스트에 아래, 오른쪽 경우만 추가를 했다.
# bfs 함수안에 들어가서 for문을 돌면서 아래, 오른쪽 방향의 값을 확인하고 이동 가능하면 이동하여 해당 위치에서 bfs 함수를 실행한다.
# 그리고 도착지에 도착하면 "HaruHaru"를 출력하고 프로그램을 종료하게 하였다.
# 그럼 도착지에 도착하지 못하는 경우에는 bfs 함수에서 나오게 된다.
# 그래서 밖에 "Hing"을 출력하게 하였다.

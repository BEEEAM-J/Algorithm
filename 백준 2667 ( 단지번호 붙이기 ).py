def dfs(x, y):
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):                          # 상하좌우의 방향을 확인
        mx, my = x + dx[i], y + dy[i]
        if 0 <= mx < N and 0 <= my < N:         # 범위를 벗어나지 않으면
            if graph[mx][my] == 1:              # 주변에 아파트가 있으면?
                cnt += 1
                graph[mx][my] = 0               # 확인한 아파트인데 나중에 이 위치에서 dfs가 돌아가면 안되서 값 변경
                dfs(mx, my)
    return cnt

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
res = 0
dfsRes = 0
apartNum = []

for x in range(N):                              # 그래프의 y축 이동
    for y in range(N):                          # 그래프의 x축 이동
        if graph[x][y] == 1:                    # 만약 해당 위치에 아파트가 있다면?
            cnt = 0
            dfsRes = dfs(x, y)
            if dfsRes == 0:                     # 이 코드에서는 단지내의 아파트가 1개만 존재하는 경우에는 값을 0을 리턴하기 때문에 직접 1을 추가해준다.
                apartNum.append(1)
                res += 1
            else:
                apartNum.append(dfsRes)         # 단지 내의 아파트의 수를 리스트에 추가
                res += 1                        # 단지 수 추가

print(res)
apartNum.sort()
for ans in apartNum:
    print(ans)

# 아파트 단지의 개수와 단지 내의 아파트의 수를 찾는 문제이다.
# 아파트의 위치가 들어있는 지도를 2차원 리스트로 입력 받는다. 
# 이 지도를 2중 for문을 돌려서 아파트가 있는 지점을 찾는다.
# 그 지점에서 dfs를 돌리는데 이 dfs는 상하좌우의 방향을 확인하면서 인접해있는 아파트가 있는지 확인을 한다.
# 만약 인접해있는 아파트가 있으면 해당 위치의 값을 0으로 바꾸고(확인한 아파트이므로 나중에 dfs가 돌아가면 안되서) 해당 위치에서 dfs를 돌린다. 
# 그리고 dfs가 다 돌고 나와지면 단지수의 카운트를 1개 올린다. 
# 이러한 과정을 반복하여 아파트 단지수와 단지 내의 아파트의 수를 찾아낸다.

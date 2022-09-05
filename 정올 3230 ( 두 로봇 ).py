def dfs(graph, start, end, visited):
    global path
    global path_length
    global path_length_d
    visited.append(start)

    if start == end:
        path += visited
        path_length += path_length_d

    for i in range(len(graph[start][0])):
        if graph[start][0][i] not in visited:
            path_length_d +=  graph[start][1][i]
            dfs(graph, graph[start][0][i], end, visited)

            # 더 갈 곳이 없는 노드이면 제거
            visited.pop(len(visited) - 1)
            path_length_d -= graph[start][1][i]   

    return path, path_length

N, robot_a, robot_b = map(int, input().split())
graph = {}
visited = []
path = []
res = []
path_length = 0
path_length_d = 0
for i in range(1, N + 1):
    graph[i] = [], []
for i in range(N - 1):
    a, b, length = map(int, input().split())

    # n번 방 = [인접 노드], [노드와의 길이] 형식으로 저장
    graph[a][0].append(b)
    graph[a][1].append(length)
    graph[b][0].append(a)
    graph[b][1].append(length)

path, path_length = dfs(graph, robot_a, robot_b, visited)

# 경로상 맞는 방으로 가기 위한 인접 방으로의 경로 길이 찾기
for i in range(len(path) - 1):
    for j in range(len(graph[int(path[i])][1])):
        if int(graph[int(path[i])][0][j]) == path[i + 1]:
            res.append(graph[int(path[i])][1][j])

if len(res) == 1:
    print(path_length - res[0])   
else:
    print(path_length - max(res))

# 로봇이 통신 할 수 있는 경우 -> 서로 인접한 방에 있어야 함
# 통신 하기 위한 최소 경로 = 로봇 사이의 전체 경로 길이 - 가장 긴 인접한 방 사이의 통로 길이
# ex) 두 로봇 사이의 경로 = [1, 2, 5, 9] -> 전체 길이 = 24
# 1 - 2 길이(8), 2 - 5 길이(10), 5 - 9 길이(6) 일때 로봇이 가장 적은 길이를 이동 해야 하기 때문에 2 - 5에서 통신 해야한다.

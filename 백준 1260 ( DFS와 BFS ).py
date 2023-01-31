def dfs(graph, start, visited = []):
    visited.append(start)               
    
    for node in graph[start]:           
        if node not in visited:
            dfs(graph, node, visited)
    
    return visited

def bfs(graph, start, visited = []):
    qlst = []
    qlst.append(start)
    
    while qlst:                         # 큐에 있는 동안
        node = qlst[0]                  # 큐는 FIFO 형식이여서 처음 요소를 추출하고, 해당 요소를 삭제한다.
        del qlst[0]
        
        if node not in visited:         # 만약 추출된 노드가 방문하지 않은 노드라면 해당 노드를 방문하고, 자식 노드들을 큐에 추가한다.
            visited.append(node)
            qlst.extend(graph[node])
    return visited           

N, M, V = map(int, input().split())     # N : 노드의 개수, M : 간선의 개수, V : 탐색 시작점
graph = {}
for _ in range(M):
    x, y = map(int, input().split())
    if x in graph:                      # 그래프를 딕셔너리에 저장하는 과정
        graph[x].append(y)
    if y in graph:
        graph[y].append(x)
    if x not in graph:
        graph[x] = [y]
    if y not in graph:
        graph[y] = [x]
        
    graph[x].sort()                     # 작은 값부터 탐색을 해야되서 정렬
    graph[y].sort()

if V not in graph:                      # 탐색 시작 노드가 그래프에 없는 경우
    print(1)
    print(1)
else:                                   # 있으면 dfs, bfs로 그래프 탐색하여 결과 출력
    dfsRes = dfs(graph, V)
    bfsRes = bfs(graph, V)
    for i in dfsRes:
        print(i, end=" ")
    print()
    for i in bfsRes:
        print(i, end=" ")

# 그래프를 입력 받아서 dfs와 bfs로 탐색 했을 때의 결과를 출력하는 문제이다. 
# 그래서 문제의 의도 그대로 그래프를 dfs, bfs로 탐색을 해서 결과를 출력하였다.
# 여기서 본인은 그래프를 key를 int로, value를 list로 가지는 딕셔너리로 받았다.
# 그리고 방문할 수 있는 노드가 여러 개인 경우에는 작은 수 부터 방문을 해야되므로 딕셔너리의 요소를 받을 때 마다 정렬을 하였다.
# 그런데 만약 탐색을 시작하는 노드가 그래프에 없는 경우를 처리하기 위해서 각 함수를 처리하기 전에 if문으로 탐색 시작 노드가 그래프에 있는지 확인하고 없으면 
# 1, 1을 출력하고, 있으면 각 함수를 실행해서 값을 출력하게 하였다.

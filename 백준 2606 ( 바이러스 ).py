def dfs(graph, start, visited = []):
#   방문한 노드 방문 처리
    visited.append(start)

#   자식노드들 확인하고 방문하지 않았으면 방문
    for n in graph[start]:
        if n not in visited:
            dfs(graph, n, visited)

    return visited

com = int(input())
node = int(input())
graph = {}

for i in range(com):
    graph[i + 1] = []

#   직접 연결된 노드들 선언
for _ in range(node):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


res = dfs(graph, 1)
#   방문한 노드 - 1이 1번 컴퓨터를 제외한 바이러스에 감염된 컴퓨터 수
print(len(res) - 1)

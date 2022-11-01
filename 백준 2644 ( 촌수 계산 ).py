def dfs(graph, start, end, visited = []):
    visited.append(start)

    for n in graph[start]:
        if end in visited:
            break
        if n not in visited:
            dfs(graph, n, end, visited)

            # 목표 노드에 도착했을 경우
            if end in visited:
                break

            # 만약 더 갈 곳이 없는 경우 왔던 노드들을 제거하면서 돌아감
            visited.pop(len(visited) - 1)
    
    return visited

n = int(input())
start, end = map(int, input().split())
m = int(input())
familyGraph = {}

for i in range(n):
    familyGraph[i + 1] = []

#   직접 연결된 노드들 선언
for _ in range(m):
    a, b = map(int, input().split())
    familyGraph[a].append(b)
    familyGraph[b].append(a)

res = dfs(familyGraph, start, end)

if end in res:
    print(len(res) - 1)
elif end not in res:
    print(-1)

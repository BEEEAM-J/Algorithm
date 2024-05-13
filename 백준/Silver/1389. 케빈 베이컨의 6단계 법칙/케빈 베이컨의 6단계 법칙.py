import sys
from collections import deque

def bfs(start, graph):
    bacon = [0] * (n + 1)
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if i not in visited:
                bacon[i] = bacon[node] + 1
                visited.append(i)
                queue.append(i)
 
    return sum(bacon)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
baconNum = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
        baconNum.append(bfs(i, graph))

print(baconNum.index(min(baconNum))+1)
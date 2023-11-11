from collections import deque

def bfs(start):
    queue = deque([start])

    while queue:
        start = queue.popleft()

        if start == K:
            return visited[start]

        for moveNode in (start - 1, start + 1, start * 2):
            if 0 <= moveNode < MaxValue and not visited[moveNode]:
                visited[moveNode] = visited[start] + 1
                queue.append(moveNode)



MaxValue = 100001
visited = [0] * MaxValue

N, K = map(int, input().split())
print(bfs(N))
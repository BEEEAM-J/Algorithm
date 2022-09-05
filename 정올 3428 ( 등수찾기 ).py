import sys
input = sys.stdin.readline

def dfs(graph, start, visited):
    count = 1
    visited[start] = True

    for node in graph[start]:
        if visited[node] is not True:
            count += dfs(graph, node, visited)

    return count

N, M, X = map(int, input().split())
up = [[] for _ in range(N + 1)]                     # 각 학생들 보다 성적이 높은 학생들
down = [[] for _ in range(N + 1)]                   # 각 학생들 보다 성적이 낮은 학생들
visited = [[False] for _ in range(N + 1)]           # dfs 방문 처리 리스트

for i in range(M):
    A, B = map(int, input().split())
    up[B].append(A)
    down[A].append(B)

u = dfs(up, X, visited)                             # X 보다 성적이 높은 학생들 수(본인 무조건 포함) -> X의 최고 등수
v = N - ((dfs(down, X, visited)) - 1)               # 전체 학생 수 - (X 보다 성적이 낮은 학생 수(본인 무조건 포함) - 1) -> X의 최저 등수

print(u, v)

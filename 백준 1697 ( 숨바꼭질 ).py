def bfs(start):
    qlst = []
    qlst.append(start)

    while qlst:
        start = qlst[0]                 # FIFO 구조 이므로 첫 번째 요소를 추출한다.
        del qlst[0]                     # 방문한 노드는 제거 (이 2줄은 deque를 사용하면 popleft로 처리 가능)

        if start == K:                  # 종료 조건
            print(visited[start])   
            exit()

        for moveNode in (start - 1, start + 1, start * 2):              # 이동하는 경우는 3가지다. +1, -1, *2
            if 0 <= moveNode < MaxValue and not visited[moveNode]:      # 범위를 벗어나지 않고, 방문하지 않은 노드라면
                visited[moveNode] = visited[start] + 1                  # 해당 노드까지 걸린 시간을 저장(전 노드까지의 시간 + 1)
                qlst.append(moveNode)                                   # 큐에 추가

MaxValue = 100001
visited = [0] * MaxValue                # 각 노드까지 도달하는데 걸린 시간을 저장할 리스트

N, K = map(int, input().split())
bfs(N)

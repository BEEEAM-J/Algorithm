def check(graph):
    global maxCnt

    for i in range(N):

        # 행으로 확인
        cnt = 1
        for j in range(N - 1):
            if graph[i][j] == graph[i][j + 1]:
                cnt += 1
                maxCnt = max(cnt, maxCnt)
            else:
                cnt = 1
    
        # 열로 확인
        cnt = 1
        for j in range(N - 1):
            if graph[j][i] == graph[j + 1][i]:
                cnt += 1
                maxCnt = max(cnt, maxCnt)
            else:
                cnt = 1

N = int(input())
graph = [list(input()) for _ in range(N)]
maxCnt = 0

# 가로로 바꾸면서 확인
for i in range(N):
    for j in range(N - 1):
        if graph[i][j] != graph[i][j + 1]:      # 만약 오른쪽과 다르면?

            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j] # 서로 바꾸고
            check(graph)                                                # 확인
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j] # 그리고 다시 돌려놓기

# 세로로 바꾸면서 확인
        if graph[j][i] != graph[j + 1][i]:      # 만약 아래와 다르다면?

            graph[j][i], graph[j + 1][i] = graph[j + 1][i], graph[j][i] # 서로 바꾸고
            check(graph)                                                # 확인
            graph[j][i], graph[j + 1][i] = graph[j + 1][i], graph[j][i] # 그리고 다시 돌려놓기

print(maxCnt)

# 그래프를 2중 for문으로 돌면서 인접한 사탕과 색이 다른 경우를 찾는다.
# 다른 경우를 찾게되면 check() 함수를 실행하게 된다.
# check() 함수에서는 오른쪽, 아래 사탕의 색과 비교를 하면서 만약 같은 색의 사탕이 있으면 먹을 수 있는 최대 사탕의 개수를 추가한다.
# check() 함수를 마치고 나면 바꿨던 사탕을 다시 원래대로 바꿔놓는다.
# 그리고 전역변수로 선언된 먹을 수 있는 최대 사탕의 개수를 출력한다.

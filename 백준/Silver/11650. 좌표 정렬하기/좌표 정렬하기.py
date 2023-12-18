import sys

N = int(sys.stdin.readline())
coordinate = [[0] for i in range(N)]

for i in range(0, N):
    nums = list(map(int, input().split()))
    coordinate[i] = nums

coordinate.sort()

for i in range(N):
    print(coordinate[i][0], coordinate[i][1])
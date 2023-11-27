canlender = [0] * 366

N = int(input())

for _ in range(N):
    S, E = map(int, input().split())

    for i in range(S, E + 1):
        canlender[i] += 1

row = 0
col = 0
total = 0

for n in range(len(canlender)):

    if canlender[n] != 0:
        col += 1
        if canlender[n] >= row:
            row = canlender[n]
        
    if canlender[n] == 0:
        total += row * col
        row = 0
        col = 0

    if canlender[n] != 0 and n == 365:
        total += row * col
print(total)
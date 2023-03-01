canlender = [0] * 366

N = int(input())

for _ in range(N):
    S, E = map(int, input().split())    

    for i in range(S, E + 1):           # 일정의 개수를 추가하는 과정
        canlender[i] += 1

row = 0
col = 0
total = 0

for n in range(len(canlender)):

    if canlender[n] != 0:               # 일정이 있는 경우
        col += 1                        # 열의 개수를 추가
        if canlender[n] >= row:         # 행이 최대인지 확인하고 최대이면 바꿈
            row = canlender[n]      
        
    if canlender[n] == 0:               # 일정이 없는 경우
        total += row * col              # 코팅지의 면적을 계산하여 추가
        row = 0
        col = 0

    if canlender[n] != 0 and n == 365:  # 달력의 처음부터 끝까지 모두 일정이 있는 경우
        total += row * col              # 계산 하고 종료
print(total)

# 달력에서 연속되는 일정들을 합쳤을 경우의 최대 가로 길이와 최대 세로 길이를 곱하면 코팅지의 넓이가 나온다. 
# 그래서 먼저 일정을 리스트로 받았는데 리스트의 요소로 일정의 개수를 받았다. 
# 그 다음에 반복문을 돌면서 일정이 있으면 가로와 세로의 값을 추가하였고, 
# 만약 일정이 없으면 이 때 코팅지의 넓이를 구하여 추가 하였다.
# 마지막의 조건은 달력의 처음부터 끝까지 모두 일정이 있는 경우 계산을 안하고 끝나는 에러를 해결하기 위해 추가하였다.   

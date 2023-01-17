tileNum = [0 for _ in range(251)]     # 각 경우에 타일이 배치되는 경우의 수들을 저장하는 리스트

tileNum[0] = 1                        # 타일 배치 경우의 수 리스트 초기 수
tileNum[1] = 1
tileNum[2] = 3

for i in range(3, 251):
    tileNum[i] = tileNum[i - 1] + (tileNum[i - 2] * 2)

while True:
    try:
        n = int(input())
        if n < 0 or n > 250:          # 입력값 n의 범위
            break

        print(tileNum[n])
    except:
        break

# 타일을 채우는 방법은 총 3가지가 있다.
# 1. 2x1 크기의 타일 1개로 1칸 채우기
# 2. 2x1 크기의 타일 2개를 가로로 배치하여 2칸 채우기
# 3. 2x2 크기의 타일 1개로 2칸 채우기

# 1번 방법으로 나오는 경우의 수는 tileNum[n - 1]이고
# 2, 3번 방법으로 나오는 경우의 수는 tileNum[n - 2] * 2 이다.
# 그래서 tileNum[i] = tileNum[i - 1] + (tileNum[i - 2] * 2) 이러한 식이 도출되고 
# 이 식으로 최대 타일 개수까지의 경우의 수를 미리 계산해놓고 입력값에 맞는 값을 출력한다.

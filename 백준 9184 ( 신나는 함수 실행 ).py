def func(a, b, c):
    if a <= 0 or b <= 0 or c <= 0: 
        return 1

    elif a > 20 or b > 20 or c > 20:
        return func(20, 20, 20)
    
    elif dp[a][b][c]:
        return dp[a][b][c]

    elif a < b and b < c:               # 연산하는 부분은 dp 리스트에 값 저장
        dp[a][b][c] = func(a, b, c-1) + func(a, b-1, c-1) - func(a, b-1, c)
        return dp[a][b][c]

    else:                               # 연산하는 부분은 dp 리스트에 값 저장
        dp[a][b][c] = func(a-1, b, c) + func(a-1, b-1, c) + func(a-1, b, c-1) - func(a-1, b-1, c-1)
        return dp[a][b][c]

dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]         # 3차원 리스트 생성

while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:         # 종료 조건
        break
    
    print("w({}, {}, {}) = {}".format(a, b, c, func(a, b, c)))

# 재귀로 돌리면 너무 오래걸리기 때문에 앞에서 계산 했던 값들을 저장하는 방법을 사용한다.(DP)
# w(a, b, c) = res 형식으로 구성되었기 때문에 3차원 리스트 dp를 만들었다. 그리고 재귀가 사용되는 부분인
# elif a < b and b < c:, else: 부분에서 계산을 하면 dp 리스트에 값을 저장하게 하였고, 조건문에서 만약에 dp 리스트에
# 저장되어있는 값이 있으면 리스트의 값을 반환하게 하여 계산 횟수를 줄였다.

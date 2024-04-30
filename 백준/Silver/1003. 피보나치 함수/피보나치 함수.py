def fibonacci(n):
    if memo[n][0] > 0:
        return memo[n][0]
    if n == 0:
        memo[n][0] = 0
        memo[n][1] = 1
        return 0
    elif n == 1:
        memo[n][0] = 1
        memo[n][2] = 1
        return 1
    else:
        memo[n][0] = fibonacci(n - 1) + fibonacci(n - 2)
        memo[n][1] = memo[n - 1][1] + memo[n - 2][1]
        memo[n][2] = memo[n - 1][2] + memo[n - 2][2]
        return memo[n][0]
    
    
t = int(input())

for _ in range(t):
    n = int(input())
    global memo
    memo = [[0, 0, 0] for _ in range(n + 1)]
    fibonacci(n)
    print(memo[n][1], memo[n][2])

# 피보나치 수를 리스트에 저장해놓고 중복되는 연산이 발생하면 이를 리스트에서 꺼내서 사용하는 방식을 사용
# 0, 1이 호출되는 횟수도 피보나치 수와 같은 방식으로 계산이 되기 때문에 리스트에 0, 1이 호출되는 횟수도 같이 저장하고 사용

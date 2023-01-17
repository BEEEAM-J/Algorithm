# PyPy3 풀이
# 피보나치 수 재귀호출 의사 코드
def fib(n):
    global fibCalcCnt                   # fib 함수 호출 횟수
    fibCalcCnt += 1                     # 호출되면 카운트 증가
    if n == 1 or n == 2:
        return 1                        # 코드 1
    else:
        fibCalcCnt -= 1                 # 코드 1을 계산한게 아니므로 카운트 감소
        return (fib(n - 1) + fib(n - 2))
    
# 피보나치 수 동적 프로그래밍 의사 코드
def fibonacci(n):
    global fibonacciCalcCnt             # fibonacci 함수 호출 횟수
    f[1], f[2] = 1, 1
    for i in range(3, n):
        f[i] = f[i - 1] + f[i - 2]      # 코드 2
        fibonacciCalcCnt += 1           # 계산하면 카운트 증가
    return fibonacciCalcCnt 


n = int(input())
f = [0 for _ in range(n)]
fibonacciCalcCnt, fibCalcCnt = 0, 0
fib(n)
fibonacci(n)
print(fibCalcCnt, fibonacciCalcCnt + 1)


# Python3 풀이
def fibonacci(n):
    global fibonacciCalcCnt             # fibonacci 함수 호출 횟수
    f[1], f[2] = 1, 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]      # 코드 2
        fibonacciCalcCnt += 1           # 계산하면 카운트 증가
    return f[n] 


n = int(input())
f = [0 for _ in range(n + 1)]
fibonacciCalcCnt, fibCalcCnt = 0, 0
res = fibonacci(n)
print(res, fibonacciCalcCnt)

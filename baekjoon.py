dictionary = {                                          # 딕셔너리 없이 사용하면 시간 초과 생김
        0: 0,
        1: 1
    }

def fibo(n):
    if n in dictionary:         
        return dictionary[n]
    else:
        res = fibo(n - 1) + fibo(n - 2)     
        dictionary[n] = res                             # 한번 계산했던 값을 딕셔너리에 저장하여 불필요한 계산 횟수 감소
        return res
    
num = int(input())
print(fibo(num))


dictionary = {
        0: 0,
        1: 1
    }

def fibo(n):
    if n in dictionary:
        return dictionary[n]
    else:
        res = fibo(n - 1) + fibo(n - 2)
        dictionary[n] = res
        return res
    
num = int(input())
print(fibo(num))

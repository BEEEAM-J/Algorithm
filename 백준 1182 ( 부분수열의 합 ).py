def func(idx, sum):
    global counter
 
    # 종료 조건
    if idx == n:
        return 0
 
    # 부분수열의 합이 s와 같은 경우
    if s == sum + a[idx]:
        counter += 1
 
    # 해당 숫자를 포함하지 않는 경우( 0 을 넣는 경우 )
    func(idx + 1, sum)        
                   
    # 해당 숫자를 포함하는 경우
    func(idx + 1, sum + a[idx])              
 
    return counter
 
n, s = map(int, input().split())
a = list(map(int, input().split()))
counter = 0
print(func(0, 0))

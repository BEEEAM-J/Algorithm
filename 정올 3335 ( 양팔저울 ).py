def func(g, idx, left, right):
 
   # 양쪽의 무게차
    value = abs(left - right)
   
    # 새롭게 구해진 값이면 list에 추가
    if value not in list_pos:
        list_pos.append(value)
 
    if idx + 1 == k:
        return 0
 
    if idx != k:
        # 추를 좌측에 놓을 때
        func(g, idx + 1, left + g[idx + 1], right)    
 
        # 추를 우측에 놓을 때
        func(g, idx + 1, left, right + g[idx + 1])    
       
        # 추를 놓지 않을 때
        func(g, idx + 1, left, right)  
 
k = int(input())
g = list(map(int, input().split()))
list_pos = []
s = sum(g)
func(g, -1, 0, 0)
 
# list_pos에 0이 들어있어서 s + 1
print((s + 1) - len(list_pos))

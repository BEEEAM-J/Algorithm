def func(g, idx, left, right):
    
    value = abs(left - right)

    if value not in list_pos:
        list_pos.append(value)

    if idx + 1 == k:
        return 0

    if idx != k:
        func(g, idx + 1, left + g[idx + 1], right)      # 추를 좌측에 놓을 때
        func(g, idx + 1, left, right + g[idx + 1])      # 추를 우측에 놓을 때
        func(g, idx + 1, left, right)   


k = int(input())
g = list(map(int, input().split()))
list_pos = [0]
s = sum(g)
func(g, -1, 0, 0)
print((s + 1) - len(list_pos))
t = int(input())

for i in range(t):
    ySum = 0
    kSum = 0

    for k in range(9):
        y, k = input().split()
        ySum += int(y)
        kSum += int(k)

    if ySum > kSum:
        print("Yonsei")
    elif kSum > ySum:
        print("Korea")
    else:
        print("Draw")
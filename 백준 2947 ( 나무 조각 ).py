num = list(map(int, input().split()))
temp = 0
x = 0
while True:
    for i in range(4):
        if num[i] > num[i + 1]:
            temp = num[i]
            num[i] = num[i + 1]
            num[i + 1] = temp
            print("{} {} {} {} {}".format(num[0], num[1], num[2], num[3], num[4]))
    for j in range(5):
        if num[j] == j + 1:
            x += 1
        else:
            pass   
    if x == 5:
        break
    else:
        x = 0

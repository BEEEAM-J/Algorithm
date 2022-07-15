def func(x):
    global counter
    if(len(x) > 1):             # x가 한자리 수가 아닐때
        counter += 1
        y = 0
        for i in x:
            y += int(i)         # x의 각 자리의 수를 단순히 더한 수 y를 만든다.
        func(str(y))

    else:                       # x가 한자리 수이면 3의배수인지 확인한다
        x = int(x)
        if(x % 3 == 0):
            print(counter)
            print("YES")
        else:
            print(counter)
            print("NO")

counter = 0

num = input()
func(num)


def func(n):
    global counter
    if(len(n) > 1):
        counter += 1
        n1 = 0
        for i in n:
            n1 += int(i)
        func(str(n1))
    
    else:
        n = int(n)
        if(n % 3 == 0):
            print(counter)
            print("YES")
        else:
            print(counter)
            print("NO")

counter = 0

num = input()
func(num)
